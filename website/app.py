from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, login_required, logout_user, current_user, LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
import ukrajinet

app = Flask(__name__)

##############
## DATABASE ##
##############

# Initialize

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/tree/Documents/02_h_da/02_Master/Siegel/WPP/Ukrajinet/ukrajinet/website/database.db'
app.config['SECRET_KEY'] = "notforproductionuseyet"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Login Management

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# User Database

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

with app.app_context():
    db.create_all()
app
###########
## FORMS ## 
###########

# Register Form

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Register")

## Check if username already exists

def validate_username(self, username):
    existing_user_username = User.query.filter_by(
        username = username.data).first()
    if existing_user_username:
        raise ValdationError("That username already exists. Please try a different one.")

# Login Form

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")

################
## APP ROUTES ##
################

@app.route('/')
def index():
    return render_template('index.html',
                            uk_wordnet = ukrajinet.retrieve_wn())

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(
            username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('working_on_uk'))

    return render_template('login.html', form=form)

@app.route('/logout/', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data) # hash password
        new_user = User(username=form.username.data, password=hashed_password) # add user 
        db.session.add(new_user) # add user to db
        db.session.commit()

        return redirect(url_for('login'))


    return render_template('register.html', form=form)

@app.route('/working-on-uk', methods=['GET', 'POST'])
@login_required

def working_on_uk():
    return render_template('working-on-uk.html')


if __name__ == '__main__':
    app.run(debug = True)

