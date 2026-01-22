from django import forms

from .models import User

from .models import Memmber

from .models import CEO

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'description', 'price']