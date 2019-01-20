from django import forms
from .models import Account, add_account
from django.contrib.auth.forms import UserCreationForm


# class UpdateAccountForm(forms.ModelForm):
#     PESEL = forms.IntegerField(required=True)
#
#     class Meta:
#         model = Account
#         fields = (
#             'PESEL',
#         )

class UpdateAccountForm(forms.Form):
    PESEL = forms.IntegerField(required=True)



class RegisterForm(UserCreationForm):
    PESEL = forms.IntegerField(required=True)

    # 
    # def save(self, commit=True):
    #     user = super(UpdateAccountForm, self).save(commit=False)
    #     user.
    #     # add_account(PESEL=123)