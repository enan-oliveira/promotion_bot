import logging
from datetime import datetime, timedelta

from data.shopee.product_offer_v2 import ProductOfferV2Object, ProductOfferNode
from integrations.shopee.shopee_affiliate_api import ShopeeAffiliateApi
from data.shopee.shopee_affiliate_queries import product_offer_v2_query
from integrations.telegram.telegram_bot_api import TelegramBotApi
from integrations.firestore.firestore_client import FirestoreClient
from firebase_functions.params import SecretParam
from firebase_admin import App as AppFirebase

class ShopeeService:

    SHOPEE_API_APP_ID = SecretParam('SHOPEE_API_APP_ID')
    SHOPEE_API_PASSWORD = SecretParam('SHOPEE_API_PASSWORD')

    TELEGRAM_BOT_TOKEN = SecretParam('TELEGRAM_BOT_TOKEN')
    TELEGRAM_CHANNEL_ID = SecretParam('TELEGRAM_CHANNEL_ID')

    FIRESTORE_COLLECTION = 'SHOPEE'

    def __init__(self, app: AppFirebase):
        self.API_SHOPEE = ShopeeAffiliateApi(
            app_id=self.SHOPEE_API_APP_ID.value,
            api_password=self.SHOPEE_API_PASSWORD.value
        )
        self.FIRESTORE_CLIENT = FirestoreClient(app)

    def _get_api_telegram(self) -> TelegramBotApi:
        return TelegramBotApi(
            bot_token=self.TELEGRAM_BOT_TOKEN.value,
            chat_id=self.TELEGRAM_CHANNEL_ID.value
        )

    def get_product_offers(self) -> ProductOfferV2Object:
        logging.info('Getting Shopee product offers...')
        return self.API_SHOPEE.get_by_query(
            query=product_offer_v2_query,
            variables={'page': 0}
        )
    
    def notify_promotions(self, product_offers: ProductOfferV2Object):
        logging.info('Notifying Shopee promotions...')
        promotions = product_offers.data.productOfferV2.nodes
        for promo in promotions:
            if not self._promo_already_sent(promo):
                self._get_api_telegram().send_photo(
                    photo_url=promo.imageUrl.__str__(),
                    caption=self._get_telegram_caption(promo),
                    link=promo.offerLink
                )
                self._set_promo_as_sent(promo)
                break
            else:
                logging.info(f'Promo: [{promo.itemId}, {promo.productName}] already sent to telegram!')

    def _get_telegram_caption(self, promo: ProductOfferNode) -> str:
        price = self._get_product_price(promo.priceMin, promo.priceMax)
        offer_link = promo.offerLink
        return f'🔥 {promo.productName}\n\n🌟 {promo.ratingStar}\n💰 {price} ({promo.priceDiscountRate}% de desconto)\n\n<a href="{offer_link}">🌐 {offer_link}</a>'

    def _get_product_price(self, price_min: str, price_max: str) -> str:
        if price_min == price_max:
            return f'R${price_min}'
        else:
            return f'R${price_min} - R${price_max}'

    def _promo_already_sent(self, promo: ProductOfferNode) -> bool:
        return self.FIRESTORE_CLIENT.exists(
            collection=self.FIRESTORE_COLLECTION,
            document=str(promo.itemId)
        )
    
    def _set_promo_as_sent(self, promo: ProductOfferNode):
        self.FIRESTORE_CLIENT.add(
            collection=self.FIRESTORE_COLLECTION,
            document=str(promo.itemId),
            data={'expires_in': datetime.now() + timedelta(days=30)}
        )
