from flask import Flask
from markupsafe import Markup
import firebase_admin
from firebase_admin import credentials,firestore
def create_app():
    app=Flask(__name__)

    app.config['SECRET_KEY']='your_secret_key'
    from app.routes import main
    app.register_blueprint(main)

    return app

