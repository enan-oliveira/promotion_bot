from firebase_admin import firestore, App as AppFirebase

class FirestoreClient:
    # TODO: add logs

    def __init__(self, app: AppFirebase):
        self.db_client = firestore.client(app=app)

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
