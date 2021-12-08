from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail, Message
import os,inspect

file_name = inspect.getfile(inspect.currentframe())
path_name=os.path.dirname(os.path.abspath(file_name))


if not os.path.exists(path_name+'/trainedModel.sav'):
    import LoanPrediction.createModel


app = Flask(__name__)

app.config['SECRET_KEY'] = 'ee556c4ef73062527783828c5651fff6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+path_name+'/site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
mail = Mail(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config.from_pyfile('config.cfg')

from LoanPrediction import routes