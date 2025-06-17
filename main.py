import os

from integrations.telegram_bot_api import TelegramBotApi
from integrations.shopee_affiliate_api import ShopeeAffiliateApi
from config.log_config import log_config
from data.shopee.shopee_affiliate_queries import product_offer_v2_query

log_config()

shopee_affiliate_api = ShopeeAffiliateApi(
    app_id=os.getenv('SHOPEE_API_APP_ID'),
    api_password=os.getenv('SHOPEE_API_PASSWORD')
)
promotions = shopee_affiliate_api.get_by_query(
    query=product_offer_v2_query,
    variables={
        'page': 0
    }
)

telegram_bot_api = TelegramBotApi(
    bot_token=os.getenv('TELEGRAM_BOT_TOKEN'),
    chat_id=os.getenv('TELEGRAM_CHANNEL_ID')
)

telegram_bot_api.send_photo(
    path_photo=r'c:\Users\SETH\Downloads\images.png', 
    message='Caption ⚡🔥', 
    link='https://pypi.org/project/requests/'
)
