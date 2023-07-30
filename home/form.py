from django import forms
class RegisterForm(forms.Form):
    username = forms.CharField(required=True, max_length=20, label= "Kullanıcı Adı")
    email = forms.EmailField(required=True, label="E-Mail")
    password = forms.CharField(max_length=20, label= "Password", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label="RePassword",widget=forms.PasswordInput)
def clean(self):
    username = self.cleaned_data.get("username")
    email = self.cleaned_data.get("email")
    password = self.cleaned_data.get("password")
    confirm = self.cleaned_data.get("confirm")


    if password and confirm and password != confirm:
        raise forms.ValidationError("Passwords dont match")

    values = {
        "username" : username,
        "email" : email,
        "password" : password,
    }
    return values