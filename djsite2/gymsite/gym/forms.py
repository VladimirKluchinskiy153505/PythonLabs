from django import forms
from django.core.validators import FileExtensionValidator

from gym.models import LessonChoice, Master


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    photo = forms.ImageField(required=False,
                             validators=[FileExtensionValidator(['jpg', 'jpeg', 'png','webp'])])
    subject_name = forms.ChoiceField(choices=LessonChoice)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Master
        fields = ['username', 'email', 'photo', 'subject_name', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match.")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
