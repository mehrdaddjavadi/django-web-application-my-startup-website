from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import Account

class RegistrationForm(UserCreationForm):

    email = forms.EmailField(max_length=255, required=True,label="",help_text="ضروری")
    phone = forms.CharField(max_length=100,required=True,label="", help_text="ترجیحا دارای شبکه های اجتماعی مانند واتساپ یا ایتا")
    class Meta:
        model = Account
        fields=('username','email','phone' ,'password1','password2')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.get(email=email)
        except Exception as e :
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.get(username=username)
        except Exception as e :
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)


        def clean_phone(self):
            phone = self.cleaned_data['phone']
            try:
                account = Account.objects.get(phone=phone)
            except Exception as e :
                return phone
            raise forms.ValidationError('Phone Number "%s" is already in use.' % phone)


class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label="رمز عبور",widget=forms.PasswordInput )

    class Meta:
        model = Account
        fields = ("email", "password")

  


    def clean(self):
       if self.is_valid():
           email = self.cleaned_data['email']
           password = self.cleaned_data['password']
           if not authenticate(email=email,password=password):
               raise forms.ValidationError(" اطلاعات برای ورود به سایت نامعتبر است")




             
