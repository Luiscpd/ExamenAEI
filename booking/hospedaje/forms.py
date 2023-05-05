from django import forms

class CreateHuesped(forms.Form):
    DPI = forms.FloatField(label="Ingrese su DPI:", widget=forms.TextInput(attrs={'class':'input'}))
    name = forms.CharField(label="Ingrese sus nombres", max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    last_name = forms.CharField(label="Ingrese sus apellidos", max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))