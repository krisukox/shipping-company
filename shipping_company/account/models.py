from django.db import models
import datetime
# from django.core.exceptions import ValidationError
# from django.utils.deconstruct import deconstructible

# @deconstructible
# class validate_range_or_null(object):
#     compare = lambda self, a, b, c: a > c or a < b
#     clean = lambda self, x: x
#     message = ('Ensure this value is between %(limit_min)s and %(limit_max)s (it is %(show_value)s).')
#     code = 'limit_value'
#
#     def __init__(self, limit_min, limit_max):
#         self.limit_min = limit_min
#         self.limit_max = limit_max
#
#     def __call__(self, value):
#         cleaned = self.clean(value)
#         params = {'limit_min': self.limit_min, 'limit_max': self.limit_max, 'show_value': cleaned}
#         print("WYWOLANE")
#         if value:  # make it optional, remove it to make required, or make required on the model
#             if self.compare(cleaned, self.limit_min, self.limit_max):
#                 raise ValidationError(self.message, code=self.code, params=params)


class Account(models.Model):
    ID_konta = models.AutoField(primary_key=True)
    PESEL = models.IntegerField(null=True)
    imie = models.CharField(max_length=40, blank=True)
    nazwisko = models.CharField(max_length=40, blank=True)
    data_zalozenia_konta = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return "ID_konta = " + self.ID_konta.__str__() + \
               ", PESEL = " + self.PESEL.__str__() + \
               ", Imie = " + self.imie.__str__() + \
               ", Nazwisko = " + self.nazwisko.__str__() + \
               ", Data zalozenia konta = " + self.data_zalozenia_konta.__str__()


class Employee(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    stanowisko = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return "ID_konta = " + self.account_id.__str__() + \
               ", stanowisko = " + self.stanowisko.__str__()


class Address(models.Model):
    ID_adresu = models.AutoField(primary_key=True)
    miasto = models.CharField(max_length=50, blank=True)
    kod_pocztowy = models.IntegerField(null=True)
    ulica = models.CharField(max_length=50, blank=True)
    nr_budynku = models.IntegerField(null=True)
    nr_lokalu = models.IntegerField(null=True)

    def __str__(self):
        return "ID_adresu = " + self.ID_adresu.__str__() + \
               ", Miasto = " + self.miasto.__str__() + \
               ", kod pocztowy = " + self.kod_pocztowy.__str__() + \
               ", Ulica = " + self.ulica.__str__() + \
               ", Numer budynku = " + self.nr_budynku.__str__() + \
               ", Numer lokalu = " + self.nr_lokalu.__str__()


class Customer(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)
    NIP = models.IntegerField(blank=True)

    def __str__(self):
        return "ID_konta = " + self.account_id.__str__() + \
               ", ID_adresu = " + self.address_id.__str__() + \
               ", NIP = " + self.NIP.__str__()


# class Driver(models.Model):
#     vehicles = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     surname = models.CharField(max_length=50)


def add_account(PESEL = None, imie = '', nazwisko = ''):
    Account(PESEL=PESEL,imie = imie,nazwisko = nazwisko).save()


def delete_account(PESEL = None, imie = '', nazwisko = ''):
    if PESEL:
        Account.objects.filter(PESEL=PESEL).delete()
    elif imie:
        Account.objects.filter(imie=imie).delete()
    elif nazwisko:
        Account.objects.filter(nazwisko=nazwisko).delete()


def get_account_id(imie,nazwisko):
    return Account.objects.filter(imie=imie, nazwisko=nazwisko)


# def add_employee(PESEL = None, imie = '', nazwisko = '',)

# def add_employee(account_id, stanowisko=''):
#     Employee(account_id = account_id)