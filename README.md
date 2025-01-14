# 🔗 ShortenX - Encurtador de URLs

ShortenX é uma aplicação simples e elegante para encurtar URLs de forma prática e rápida. Desenvolvido com **Python** e **Flask**, este projeto foi pensado para ser intuitivo, funcional e de fácil utilização.

## 🚀 Funcionalidades

- ✂️ Encurtar URLs longas para versões curtas e simples.
- 🌐 Redirecionamento automático ao acessar a URL encurtada.
- 💡 Interface responsiva e estilosa com **Bootstrap**.
- 🔥 Fácil de configurar e rodar localmente.

---

## 🛠️ Tecnologias Utilizadas

- **Python** 🐍
- **Flask** (Framework Backend)
- **Flask-Migrate** (Gerenciamento de Migrações)
- **SQLite** (Banco de Dados)
- **Bootstrap** (Estilização Frontend)
- **HTML5 + CSS3** (Estrutura e Estilo)

---

## 🖥️ Como Rodar o Projeto

### Pré-requisitos

- **Python 3.10+** instalado
- **Virtualenv** para isolar dependências

### Passos

1. Clone o repositório:

```bash
git clone https://github.com/O-Farias/ShortenX.git
cd ShortenX
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```


4. Configure o banco de dados:

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

5. Rode a aplicação:

```bash
flask run
```

6. Acesse no navegador:

```bash
http://127.0.0.1:5000
```

### 🎨 Personalização

- O arquivo `styles.css` permite personalizar o design.
- Para mudar o banco de dados, edite a variável `DATABASE_URL` no arquivo `.env`.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
