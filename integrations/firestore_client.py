import firebase_admin
from firebase_admin import credentials, firestore

class FirestoreClient:
    # TODO: add logs

    def __init__(self, certificate_path: str):
        self._initialize_firebase(certificate_path)
        self.db_client = firestore.client()

    def _initialize_firebase(self, certificate_path: str):
        if not firebase_admin._apps:
            firebase_admin.initialize_app(
                credentials.Certificate(certificate_path)
            )

    def add(self, collection: str, document: str, data: dict):
        doc_ref = self.db_client.collection(collection).document(document)
        doc_ref.set(data)

    def exists(self, collection: str, document: str):
        doc_ref = self.db_client.collection(collection).document(document)
        doc = doc_ref.get()
        return doc.exists

    def delete(self, collection: str, document: str):
        doc_ref = self.db_client.collection(collection).document(document)
        doc_ref.delete()
