import requests
import logging
import hashlib
import time
import json

from data.shopee.product_offer_v2 import ProductOfferV2Object

class ShopeeAffiliateApi:

    BASE_URL = 'https://open-api.affiliate.shopee.com.br/graphql'

    def __init__(self, app_id: str, api_password: str):
        self.API_APP_ID = app_id
        self.API_PASSWORD = api_password

    @property
    def timestamp(self) -> int:
        return int(time.time())
    
    def get_by_query(self, query: str, variables: dict) -> ProductOfferV2Object:
        logging.info(f'Executing query shopee...')
        timestamp = self.timestamp
        payload_str = self.get_payload_str(query, variables)
        signature = self.get_signature(timestamp, payload_str)
        headers = self.get_headers(timestamp, signature)
        response = requests.post(
            self.BASE_URL, 
            headers=headers, 
            data=payload_str
        )
        response.raise_for_status()
        return ProductOfferV2Object.model_validate(response.json())

    def get_payload_str(self, query: str, variables: dict) -> str:
        payload = {
            'query': query,
            'variables': variables
        }
        return json.dumps(payload, separators=(',', ':'))

    def get_signature(self, timestamp: int, payload: str) -> str:
        factor = f'{self.API_APP_ID}{timestamp}{payload}{self.API_PASSWORD}'
        return hashlib.sha256(factor.encode()).hexdigest()

    def get_headers(self, timestamp: int, signature: str) -> dict:
        return {
            'Content-Type': 'application/json',
            'Authorization': f'SHA256 Credential={self.API_APP_ID},Timestamp={timestamp},Signature={signature}'
        }
