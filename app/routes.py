from flask import Blueprint, render_template, request, redirect
from app.models import URL
from app.database import db

shortener_bp = Blueprint('shortener', __name__, template_folder="../templates")

@shortener_bp.route('/')
def home():
    return render_template('home.html')

@shortener_bp.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form.get('original_url')

    if not original_url:
        return render_template('home.html', error="URL inválida. Tente novamente.")

    short_url = URL.generate_short_url()
    new_url = URL(original_url=original_url, short_url=short_url)

    with db.session.begin():
        db.session.add(new_url)

    return render_template('home.html', short_url=short_url, original_url=original_url)

@shortener_bp.route('/<short_url>')
def redirect_to_url(short_url):
    url = URL.query.filter_by(short_url=short_url).first()

    if url:
        return redirect(url.original_url)
    else:
        return render_template('home.html', error="URL não encontrada.")
