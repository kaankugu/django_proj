from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class KayitForm(UserCreationForm):
    username = forms.CharField(max_length=100, label="Kullanıcı adı")
    password1 = forms.CharField(max_length=100, label="Parola")
    password2 = forms.CharField(max_length=100, label="Parola doğrulama")
    is_seller = forms.ChoiceField(choices=[('user', 'User'), ('admin', 'Admin')], label='Kullanıcı Türü')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'is_seller')

    def clean_is_seller(self):
        is_seller = self.cleaned_data.get('is_seller')
        print("clean_is_seller metodu çağrıldı") # eklediğimiz print komutu
        print("is_seller değeri:", is_seller) # eklediğimiz print komutu

        if is_seller not in ['user', 'admin']:
            raise forms.ValidationError('Geçersiz kullanıcı türü.')

        return is_seller
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Parola eşleşmedi. Bir daha deneyin.")
        return password2


    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_seller = self.cleaned_data["is_seller"]

        if commit:
            user.save()
        return user
