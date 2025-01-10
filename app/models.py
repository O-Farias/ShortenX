from app import db
import string
import random

class URL(db.Model):
    __tablename__ = 'url'

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048), nullable=False)
    short_url = db.Column(db.String(6), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp(), nullable=False)

    @staticmethod
    def generate_short_url():
        """Gera um identificador único para a URL."""
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=6))
