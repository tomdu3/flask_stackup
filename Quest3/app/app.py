from flask import Flask, request, render_template, redirect, url_for
from models import Product, User, db
from controllers.users import get_users, get_user, add_user, update_user, delete_user, get_user_by_username
from controllers.products import get_products, get_product, add_product, update_product, delete_product
from sqlalchemy import exc
import hashlib
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from werkzeug.utils import secure_filename
import secrets

app = Flask(__name__, template_folder = 'templates', static_folder = 'static')
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)