from app import db
class User(db.Model):
  """An admin user capable of viewing reports.

  :param str email: email address of user
  :param str password: encrypted password for the user

  """
  __tablename__ = 'user'

  email = db.Column(db.String, primary_key=True)
  first_name = db.Column(db.String)
  last_name = db.Column(db.String)
  password = db.Column(db.String)
  authenticated = db.Column(db.Boolean, default=False)
  ballance = db.Column(db.Float)

  def is_active(self):
    """True, as all users are active."""
    return True

  def get_id(self):
    """Return the email address to satisfy Flask-Login's requirements."""
    return self.email

  def is_authenticated(self):
    """Return True if the user is authenticated."""
    return self.authenticated

  def is_anonymous(self):
    """False, as anonymous users aren't supported."""
    return False

  def get_ballance(self):
    return self.ballance

  def get_firstname(self):
    return self.first_name

  def get_lastname(self):
    return self.last_name

  def __init__(self, email, password, first_name, last_name):
    self.email = email
    self.password = password
    self.first_name = first_name
    self.last_name = last_name
    self.ballance = 500.00
