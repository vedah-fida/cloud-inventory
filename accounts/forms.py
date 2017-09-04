from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.models import User

User = get_user_model()



class UserForm(forms.ModelForm):
    username = forms.CharField(label="Enter Your Username")
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:  # information about your class
        model = User
        fields = ['username', 'password']

        def clean(self, *args, **kwargs):
            username = self.cleaned_data.get('username')
            username_qs = User.objects.filter(username=username)
            if username_qs.DoesNotExist():
                raise forms.ValidationError("User is not registered")
            return super(UserForm, self).clean(*args, **kwargs)

