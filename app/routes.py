from flask import Blueprint, render_template, request, redirect
from app.models import URL
from app import db
import traceback

# Blueprint para rotas
shortener_bp = Blueprint('shortener', __name__, template_folder="../templates")

@shortener_bp.route('/')
def home():
    """Rota para exibir a página inicial."""
    return render_template('home.html')

@shortener_bp.route('/shorten', methods=['POST'])
def shorten_url():
    """Rota para encurtar uma URL."""
    try:
        # Obtém a URL original do formulário
        original_url = request.form.get('original_url')

        # Verifica se a URL é válida
        if not original_url or not original_url.strip():
            return render_template('home.html', error="URL inválida. Por favor, insira uma URL válida.")

        # Gera um identificador curto para a URL
        short_url = URL.generate_short_url()
        
        # Cria e salva a nova URL no banco de dados
        new_url = URL(original_url=original_url, short_url=short_url)
        with db.session.begin():  # Contexto explícito para transação
            db.session.add(new_url)

        # Retorna para a página inicial com o link encurtado
        return render_template('home.html', short_url=short_url, original_url=original_url)

    except Exception as e:
        # Log de erro detalhado para depuração
        print("Erro ao encurtar URL:", traceback.format_exc())
        return render_template('home.html', error="Ocorreu um erro ao processar sua solicitação. Tente novamente.")

@shortener_bp.route('/<short_url>')
def redirect_to_url(short_url):
    """Rota para redirecionar uma URL encurtada."""
    try:
        # Busca a URL original correspondente no banco de dados
        url = URL.query.filter_by(short_url=short_url).first()

        # Redireciona para a URL original, se encontrada
        if url:
            return redirect(url.original_url)
        else:
            return render_template('home.html', error="URL não encontrada.")
    
    except Exception as e:
        # Log de erro detalhado para depuração
        print("Erro ao redirecionar URL:", traceback.format_exc())
        return render_template('home.html', error="Ocorreu um erro ao redirecionar a URL.")
