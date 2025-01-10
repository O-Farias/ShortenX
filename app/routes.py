from flask import Blueprint, request, jsonify, redirect
from app.models import URL
from app.database import db

shortener_bp = Blueprint('shortener', __name__)

@shortener_bp.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.json
    original_url = data.get('original_url')

    if not original_url:
        return jsonify({'error': 'URL inválida'}), 400

    short_url = URL.generate_short_url()
    new_url = URL(original_url=original_url, short_url=short_url)
    db.session.add(new_url)
    db.session.commit()

    return jsonify({'original_url': original_url, 'short_url': short_url})

@shortener_bp.route('/<short_url>')
def redirect_to_url(short_url):
    url = URL.query.filter_by(short_url=short_url).first()

    if url:
        return redirect(url.original_url)
    else:
        return jsonify({'error': 'URL não encontrada'}), 404
