from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # Carregar variáveis de ambiente
    load_dotenv()

    # Inicializando o Flask app
    app = Flask(__name__)

    # Definir caminho absoluto para o banco de dados SQLite
    db_path = os.getenv('DATABASE_URL', os.path.join(os.path.abspath(os.getcwd()), 'instance', 'shortify.db'))
    if db_path.startswith('sqlite:///'):
        db_path = f"sqlite:///{os.path.abspath(db_path[10:])}"

    print(f"Carregando DATABASE_URL: {db_path}")  # Para depuração

    # Configuração do SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar extensões
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar blueprints
    from app.routes import shortener_bp
    app.register_blueprint(shortener_bp)

    return app
