from django import forms
from .models import UserSignUp,mynotes,feedback

class UserSignUpForm(forms.ModelForm):
    class Meta:
        model=UserSignUp
        fields='__all__'   
        # fields=['username','password']#cleandata     

class mynotesForm(forms.ModelForm):
    class Meta:
        model=mynotes
        fields='__all__'


class feedbackForm(forms.ModelForm):
    class Meta:
        model=feedback
        fields='__all__'