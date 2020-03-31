from django import forms
from django.contrib.auth.models import User
from . models import UserProfileInfo


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password')

		labels = {
			'username':'Usuario',
			'email':'Correo',
			
		}

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')

        labels = {
        	'portfolio_site':"Sito Web",
        	'profile_pic':'Foto de perfil',
        }
    