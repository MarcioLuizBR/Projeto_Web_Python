from flask import Flask, render_template, url_for
from forms import FormCriarConta, FormLogin

app = Flask(__name__)

lista_usuarios = ['Marcio', 'Luiz', 'Ana', 'Kelen', 'Samuel', 'Aquilles']

# lembrete pessoal - executar 'python' no terminal, depois 'import secrets' e 'secrets.token_hex(16), depois sair do python com 'exit()'
app.config['SECRET_KEY'] = 'cd1b5eede7d3dd4eb7950bf8b0602635'

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/login')
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)

if __name__ == '__main__':
    app.run(debug=True)

