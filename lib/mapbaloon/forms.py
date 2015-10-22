from django.forms import *
from django.forms.extras.widgets import *

class SignupForm(forms.Form):
	login = CharField(max_length = 16, widget = TextInput)
	mail = EmailField(widget = EmailInput)
	password = CharField(max_length = 32, widget = PasswordInput)
	confirm_password = CharField(max_length = 32, widget = PasswordInput)

class SigninForm(forms.Form):
        login = CharField(max_length = 16, widget = TextInput)
        password = CharField(max_length = 32, widget = PasswordInput)

