from django.forms import CharField, PasswordInput, ModelForm, EmailInput, BooleanField, CheckboxInput
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CreateUserForm(ModelForm):
    username = CharField(required=True, label='Username')
    password = CharField(widget=PasswordInput(), required=True, label='Password')
    email = CharField(widget=EmailInput(), required=True, label='E-mail')
    first_name = CharField(required=True, label='First name')
    last_name = CharField(required=True, label='Last name')

    helper = FormHelper()
    helper.form_class = "col z-depth-3"
    helper.add_input(Submit('submit', 'Create new user', css_class='btn waves-effect waves-light'))
    helper.form_method = 'POST'

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
