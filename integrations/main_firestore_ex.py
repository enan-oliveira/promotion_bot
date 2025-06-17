from firestore_client import FirestoreClient
from datetime import datetime, timedelta

firestore_client = FirestoreClient('/home/seth/Documents/python/firestore_db/development-70c26-firebase-adminsdk-fbsvc-12adc9c3e5.json')

firestore_client.add(
    collection='shopee',
    document='hash1',
    data={
        'item': 'shopee_bike',
        'type': 'bycicle',
        'expires_in': datetime.now() + timedelta(days=15)
    }
)

firestore_client.add(
    collection='shopee',
    document='hash2',
    data={
        'item': 'shopee_bike',
        'type': 'bycicle',
        'expires_in': datetime.now() + timedelta(days=15)
    }
)

firestore_client.exists(
    collection='shopee',
    document='hash1',
)

firestore_client.delete(
    collection='shopee',
    document='hash1'
)

firestore_client.exists(
    collection='shopee',
    document='hash1'
)
