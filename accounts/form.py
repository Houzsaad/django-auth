from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from .models import User

from .models import Memmber

from .models import CEO

class CEOForm(forms.ModelForm):
    class Meta:
        model = CEO
        fields = [ 'name', 'locality' ]

class RegistrationForm(UserCreationForm):
    gmail = forms.EmailField(
        max_length=90,        
        required=True
        #helper_text='required'
    )

    first_name = forms.CharField(
        max_length=30,
        required=True
        #helper_text='required'
    )
    last_name = forms.CharField(
        max_length=30,
        required=True
        #helper_text='required'
    )
    phone_number = forms.CharField(
        max_length=15,
        required=True,
    )
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'gmail', 'phone_number', 'password1', 'password2')

    def clean_gmail(self):
        gmail = self.cleaned_data.get('gmail')
        if User.objects.filter(gmail=gmail).exists():
            raise forms.ValidationError("This email address is already in use.")
        return gmail
    def save(self, commit=True):
        user = super().save(commit=False)
        user.gmail = self.cleaned_data['gmail']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()
        return user