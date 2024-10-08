from flask import Flask
from flask_login import LoginManager
from .config import Configuration
from .models import db, Employee
from .routes import orders

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(orders.bp)
db.init_app(app)  # Configure the application with SQLAlchemy

login = LoginManager(app)
login.login_view = "session.login"


@login.user_loader
def load_user(id):
    return Employee.query.get(int(id))
