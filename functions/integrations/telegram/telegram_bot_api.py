import logging
import requests

class TelegramBotApi:

    BASE_URL = 'https://api.telegram.org'

    def __init__(self, bot_token: str, chat_id: str):
        self.BOT_TOKEN = bot_token
        self.CHAT_ID = chat_id

    def send_message(self, message: str):
        logging.info(f'Sending message [{message}] to chat [{self.CHAT_ID}]...')

        requests.post(
            url=f'{self.BASE_URL}/bot{self.BOT_TOKEN}/sendMessage',
            data={
                'chat_id': self.CHAT_ID,
                'text': message
            }
        ).raise_for_status()

    def send_photo(self, photo_url: str, caption: str, link: str = ''):
        logging.info(f'Sending photo URL [{photo_url}] to chat [{self.CHAT_ID}]...')
        
        requests.post(
            url=f'{self.BASE_URL}/bot{self.BOT_TOKEN}/sendPhoto',
            data={
                'chat_id': self.CHAT_ID,
                'photo': photo_url,
                'caption': caption,
                'parse_mode': 'HTML'
            }
        ).raise_for_status()
