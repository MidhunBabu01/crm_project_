from django import forms
from crm_app.models import Companies, Client



class CompaniForm(forms.ModelForm):
    class Meta:
        model = Companies
        fields = '__all__'



class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        