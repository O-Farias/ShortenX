from app.database import db
import string
import random

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048), nullable=False)
    short_url = db.Column(db.String(6), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())

    @staticmethod
    def generate_short_url():
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=6))
