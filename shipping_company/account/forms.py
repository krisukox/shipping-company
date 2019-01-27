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

class AddTimetable(forms.Form):
    data_poczatek = forms.DateField(required=True)
    data_koniec = forms.DateField(required=True)


class EmployeeRegisterForm(UserCreationForm):
    stanowisko = forms.CharField(max_length=40, required=True)


class UpdateAccountForm(forms.Form):
    PESEL = forms.IntegerField(required=True)



class RegisterForm(UserCreationForm):
    PESEL = forms.IntegerField(required=True)


class DriverRegisterForm(UserCreationForm):
    doswiadczenie = forms.IntegerField(required=True)
    kat_prawa_jazdy = forms.CharField(max_length=20, required=True)

    # 
    # def save(self, commit=True):
    #     user = super(UpdateAccountForm, self).save(commit=False)
    #     user.
    #     # add_account(PESEL=123)