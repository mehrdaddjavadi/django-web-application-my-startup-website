from django import forms
from .models import EmailForMagazine


class EmailForMagazineForm(forms.ModelForm):
    email=forms.EmailField(widget=forms.TextInput(attrs={
        "type":"email",
        "class" :"form-control",
        "id" : "email",
         "name":"email",
          "placeholder":"              رایانامه",
    }), label="")
    class Meta:
        model = EmailForMagazine
        fields = ("email",)

