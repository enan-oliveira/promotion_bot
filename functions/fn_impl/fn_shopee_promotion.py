from firebase_functions import scheduler_fn
from firebase_admin import initialize_app

from service.shopee.shopee_service import ShopeeService

app = initialize_app(name='fn_cron_shopee')

@scheduler_fn.on_schedule(schedule='*/15 * * * *')
def send_shopee_promotion(_: scheduler_fn.ScheduledEvent):

    service = ShopeeService(app)
    product_offers = service.get_product_offers()
    service.notify_promotions(product_offers)
