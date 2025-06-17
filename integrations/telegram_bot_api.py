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

    def send_photo(self, path_photo: str, message: str='', link: str=''):
        logging.info(f'Sending photo [{path_photo}] to chat [{self.CHAT_ID}]...')

        with open(path_photo, 'rb') as photo_bytes:
            requests.post(
                url=f'{self.BASE_URL}/bot{self.BOT_TOKEN}/sendPhoto',
                data={
                    'chat_id': self.CHAT_ID,
                    'caption': f'<a href="{link}">{link}</a>\n\n{message}' if link else message,
                    'parse_mode': 'HTML'
                },
                files={
                    'photo': photo_bytes
                }
            ).raise_for_status()
