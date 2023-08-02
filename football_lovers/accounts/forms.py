from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter password...'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password...'

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'email',)

        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Enter Username...'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Enter Email...'}
            ),
            'profile_picture': forms.URLInput(
                attrs={'placeholder': 'Link to Image...'}
            ),
        }

        labels = {
            'profile_picture': 'Profile Image URL',
        }


class EditUserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name', 'email', 'gender', 'profile_picture',)

        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Enter Username...'}
            ),
            'first_name': forms.TextInput(
                attrs={'placeholder': 'Enter First Name...'}
            ),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Enter Last Name...'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Enter Email...'}
            ),
            'profile_picture': forms.URLInput(
                attrs={'placeholder': 'Link to Image...'}
            ),
        }

        labels = {
            'profile_picture': 'Profile Image URL',
        }
