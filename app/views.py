from flask import render_template, redirect, url_for, request
from flask_nav import Nav
from app.nav import nav, nav_authenticated
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from flask_login import login_required, login_user, logout_user, current_user
from app.forms import LoginForm, CreateAccountForm, TransferForm
from app import db
from app.models import User
from app import login_manager
from app import app
import logging


nav.register_element('frontend_top', Navbar(
  # TODO: CLEAN UP NAV BAR
  View('CC_Bank', '.index'),
  View('Create Account', '.Create_account'),
  View('User summary', '.User_Home'),
  View('transfer', '.transfer'),
  View('login', '.login'),
  View('logout', '.logout'),))


@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html', Title='CC Bank')


@app.route('/login', methods=['GET', 'POST'])
def login():
  # Here we use a class of some kind to represent and validate our
  # client-side form data. For example, WTForms is a library that will
  # handle this for us, and we use a custom LoginForm to validate.
  form = LoginForm()
  if form.validate_on_submit():
    # Login and validate the user.
    user = User.query.get(form.email.data)
    # user should be an instance of your `User` class
    if user:
      if user.password == form.password.data:
        user.authenticated = True
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)
        return redirect(url_for("User_Home"))
  return render_template("login.html", form=form, user=current_user)


@app.route("/logout", methods=["GET"])
@login_required
def logout():
  """Logout the current user."""
  user = current_user
  user.authenticated = False
  db.session.add(user)
  db.session.commit()
  logout_user()
  return render_template("logout.html", user=current_user)


@login_manager.user_loader
def user_loader(user_id):
  """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve
    """
  return User.query.get(user_id)


@app.route('/transfer', methods=['GET', 'POST'])
@login_required
def transfer():
  amount = request.values.get('amount')
  to_user = request.values.get('transfer_to')
  print(amount, to_user)
  print(current_user.is_authenticated())
  logging.basicConfig(format='%(asctime)s %(message)s',
                      filename='transactions.log', level=logging.INFO)
  form = TransferForm()
  if form.validate_on_submit():
    transfer_to_user = User.query.get(form.transfer_to.data)
    current_user.ballance -= form.Ammount.data
    transfer_to_user.ballance += form.Ammount.data
    logging.info('%s %s transferred $%s to %s %s ', current_user.first_name,
                 current_user.last_name, form.Ammount.data,
                 transfer_to_user.first_name, transfer_to_user.last_name)
    db.session.commit()
    return redirect(url_for("User_Home"))
  if amount and to_user:
    transfer_to_user = User.query.get(to_user)
    current_user.ballance -= float(amount)
    transfer_to_user.ballance += float(amount)
    logging.info('%s %s transferred $%s to %s %s ', current_user.first_name,
                 current_user.last_name, form.Ammount.data,
                 transfer_to_user.first_name, transfer_to_user.last_name)
    db.session.commit()
  return render_template("transfer.html", user=current_user, form=form)


@app.route('/User_Home', methods=['GET', 'POST'])
@login_required
def User_Home():
  return render_template("User_Home.html", user=current_user)


@app.errorhandler(403)
@login_manager.unauthorized_handler
def unauthorized():
  return render_template("unauthorized.html", user=current_user)


@app.route('/Create_account', methods=['GET', 'POST'])
def Create_account():
  logging.basicConfig(format='%(asctime)s %(message)s',
                      filename='account_creation.log', level=logging.INFO)
  form = CreateAccountForm()
  if form.validate_on_submit():
    u = User(form.email.data, form.password.data, form.firstname.data,
             form.lastname.data)
    db.session.add(u)
    db.session.commit()
    logging.info('%s %s has created an account with the email %s',
                 form.firstname.data, form.lastname.data, form.email.data)
    user = User.query.get(form.email.data)

    # user should be an instance of your `User` class
    if user:
      if user.password == form.password.data:
        user.authenticated = True
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)
        return redirect(url_for("User_Home"))
  return render_template("create_account.html", form=form, user=current_user)
