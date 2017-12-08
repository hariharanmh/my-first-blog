from django import forms
from django.contrib.auth import get_user_model
from .models import Shop

User = get_user_model()

class ShopModelForm(forms.ModelForm):
	class Meta:
		model  = Shop
		fields = [
			'shop_name', 
			'shop_phone_number', 
			'shop_city', 
			'shop_address', 
			'shop_category', 
			'shop_type',
		]

class RegisterModelForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model  = User
        fields = ('username', 'email',)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("Cannot use this email. It's already registered")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        #print(password2)
        return password2

    def save(self, commit=True):
        User = super(RegisterModelForm, self).save(commit=False)
        User.set_password(self.cleaned_data["password1"])
        #print(User)
        User.is_active = False
       

        if commit:
            User.save()
            #User.profile.send_activation_email()
        return User