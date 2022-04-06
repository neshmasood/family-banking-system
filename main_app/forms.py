from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



ROLE_CHOICES= [
    ('parent/guardian', 'Parent/Guardian'),
    ('child', 'Child')
    ]

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    role = forms.CharField(label='What is your role?', widget=forms.Select(choices=ROLE_CHOICES))




    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'role', 'password1', 'password2' )
