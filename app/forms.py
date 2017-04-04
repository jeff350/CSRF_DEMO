from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField, \
    validators, ValidationError, PasswordField, IntegerField, FormField, \
    SelectMultipleField, FieldList, widgets
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
from types import *


class LoginForm(FlaskForm):
    email = StringField()
    password = PasswordField()
    submit = SubmitField("Submit")


class TransferForm(FlaskForm):
    transfer_to = StringField('Enter the email address of the user you would '
                              'like to transfer funds to: ',
                              [validators.DataRequired('Enter the username of the user to transfer money to')])
    Ammount = IntegerField('Transfer Amount:',
                           [validators.NumberRange(min=0), validators.DataRequired('Enter the amount to transfer')])
    submit = SubmitField("Submit")


class CreateAccountForm(FlaskForm):
    firstname = StringField('First Name:', [validators.DataRequired('enter your '
                                                                    'First Name'), ], )
    lastname = StringField('Last Name:', [validators.DataRequired('enter your '
                                                                  'Last Name'), ], )
    email = StringField('Email:', [validators.email('Please enter a valid '
                                                    'Email '
                                                    'address'),
                                   validators.DataRequired('enter your '
                                                           'Email'), ], )
    password = PasswordField('Password:', [validators.DataRequired('enter your '
                                                                   'Password'), ], )
    submit = SubmitField("Submit")

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
