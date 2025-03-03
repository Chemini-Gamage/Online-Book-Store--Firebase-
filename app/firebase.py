
import firebase_admin
from firebase_admin import credentials, firestore

   #firebase
cred=credentials.Certificate("config/firebase_credentials.json")
firebase_admin.initialize_app(cred)
    #initialize firestore db
db=firestore.client()
