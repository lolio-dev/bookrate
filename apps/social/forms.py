from django import forms


class CustomTextInput(forms.TextInput):
    def __init__(self, placeholder, full_width=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs['placeholder'] = placeholder
        if full_width:
            self.attrs['class'] = 'w-full'


class CustomPasswordInput(forms.PasswordInput):
    def __init__(self, placeholder, full_width=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs['placeholder'] = placeholder
        if full_width:
            self.attrs['class'] = 'w-full'


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", widget=CustomTextInput(placeholder="Your awesome username"))
    password = forms.CharField(label="Password", widget=CustomPasswordInput(placeholder="Your magic password"))


class SignupForm(forms.Form):
    email = forms.EmailField(label="Email", widget=CustomTextInput(placeholder="Your email"))
    username = forms.CharField(label="Username", widget=CustomTextInput(placeholder="Your username"))
    password = forms.CharField(label="Password", widget=CustomPasswordInput(placeholder="Your password"))
    password_validation = forms.CharField(
        label="Password validation",
        widget=CustomPasswordInput(placeholder="Repeat again")
    )
    gcu_check = forms.BooleanField(label="Accept gcu")
