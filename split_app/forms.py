from django import forms
from split_app.models import bill, payee

class payeeForm(forms.ModelForm):
    
    class Meta:
        model = payee
        fields = ("name","mobile")
