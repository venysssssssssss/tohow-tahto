import os

import bcrypt
import click
from dotenv import load_dotenv
from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)
from flask_login import (LoginManager, UserMixin, login_required, login_user,
                         logout_user)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db = SQLAlchemy(app)

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Specify the login route


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(
        db.String(80), nullable=False
    )  # Store hashed password

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(
            password.encode('utf-8'), bcrypt.gensalt()
        )

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.cli.command('initdb')
def initdb_command():
    """Initialize the database."""
    click.echo('Initializing the database')
    db.create_all()
    click.echo('Database initialized')


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password')  # Generic message for security

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        # Validate all fields and passwords
        errors = []
        if not all([username, email, password, confirm_password]):
            errors.append('All fields are required')
        if password != confirm_password:
            errors.append('Passwords do not match')

        if errors:
            flash(' '.join(errors))  # Display all errors in one message
            return render_template('register.html')

        try:
            user = User(username=username, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash(f'New user {username} registered successfully!')
            return redirect(url_for('login'))
        except IntegrityError as e:
            db.session.rollback()
            if 'UNIQUE constraint failed: user.email' in str(e):
                flash('Email already in use')
            elif 'UNIQUE constraint failed: user.username' in str(e):
                flash('Username already in use')
            else:
                flash('Registration error')  # Generic message for security
            return render_template('register.html')

    return render_template('register.html')


@app.route('/index')
@login_required
def index():
    return render_template('index.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/tools')
@login_required
def tools():
    return render_template('tools.html')


@app.route('/datatable_ft')
@login_required
def ftplat():
    return render_template('datatable_ft.html')


@app.route('/process_demand', methods=['POST'])
@login_required
def process_demand():
    option_selected = request.form.get('options_ft')

    # Renderiza o template HTML apropriado com base na opção selecionada
    if option_selected == 'Criar novo(s) skill(s)':
        return render_template('novo_skill_ft.html')
    elif option_selected == 'Roteamento':
        return render_template('datatable_ft.html')
    # Adicione mais casos conforme necessário para cada opção

    # Se a opção selecionada não for reconhecida, redirecione para uma página de erro ou retorne uma mensagem de erro
    return 'Opção não reconhecida'


if __name__ == '__main__':
    app.run(debug=True)
