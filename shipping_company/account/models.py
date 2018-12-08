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


class Driver(models.Model):
    ID_kierowcy = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    kat_prawa_jazdy = models.CharField(max_length=20, blank=False, null=False,default=0)
    doswiadczenie = models.IntegerField(null=False,default=0)


    def __str__(self):
        return "ID_kierowcy = " + self.ID_kierowcy.__str__() + \
               "ID_konta = " + self.account.__str__() + \
                "Kat prawa jazdy " + self.kat_prawa_jazdy.__str__() + \
                "Dowswiadczenie " + self.doswiadczenie.__str__()


class Service(models.Model):
    ID_uslugi = models.AutoField(primary_key = True)
    opis_uslugi = models.CharField(max_length = 100, blank=False, null=False)
    koszt = models.IntegerField(blank=False, null=False)


    def __str__(self):
        return "ID_uslugi = " + self.ID_uslugi.__str__() + \
               "opis_uslugi = " + self.opis_uslugi.__str__() + \
               "koszt " + self.koszt.__str__()


class OrdersHistory(models.Model):
    ID_zamowienia = models.AutoField(primary_key = True)
    ID_konta = models.ForeignKey(Account, on_delete = models.SET_NULL, blank=False,null=True)
    ID_uslugi = models.ForeignKey(Service , on_delete = models.SET_NULL, blank=False, null=True)
    ID_adresu_pocz = models.ForeignKey(Address , on_delete = models.SET_NULL, related_name="ID_adresu_pocz",blank=False, null=True)
    ID_adresu_kon = models.ForeignKey(Address, on_delete = models.SET_NULL,related_name="ID_adresu_kon" ,blank=False, null=True)

    def __str__(self):
        return "ID_zamowienia = " + self.ID_zamowienia.__str__() + \
               "ID_konta = " + self.ID_konta.__str__() + \
               "Kat ID_uslugi jazdy " + self.ID_uslugi.__str__() + \
               "ID_adresu_pocz " + self.ID_adresu_pocz.__str__() + \
               "ID_adresu_kon " + self.ID_adresu_kon.__str__()


class Vehicle(models.Model):
    Nr_rej = models.CharField(max_length = 20, primary_key = True)
    marka = models.CharField(max_length = 40, blank=True,null=True)
    model = models.CharField(max_length=40, blank=True, null=True)
    atrybut = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
            return "Nr_rej = " + self.Nr_rej.__str__() + \
                   "marka = " + self.marka.__str__() + \
                   "model " + self.model.__str__() + \
                   "atrybut " + self.atrybut.__str__()

class Timetable(models.Model):
    ID_terminu = models.AutoField(primary_key = True)
    data_pocz = models.DateField(blank = False, null=False)
    data_kon = models.DateField(blank = False, null=False)
    ID_kierowcy = models.ForeignKey(Driver, on_delete = models.SET_NULL, blank = False, null=True)
    ID_zamowienia = models.ForeignKey(Service, on_delete=models.SET_NULL, blank=False, null=True)

    def __str__(self):
            return "ID_terminu = " + self.ID_terminu.__str__() + \
                   "data_pocz = " + self.data_pocz.__str__() + \
                   "data_kon " + self.data_kon.__str__() + \
                   "ID_kierowcy " + self.ID_kierowcy.__str__() + \
                    "ID_zamowienia " + self.ID_zamowienia.__str__()

class Drivers_Vehicles(models.Model):
    ID_kierowcy = models.ManyToManyField(Driver)
    Nr_rej = models.ManyToManyField(Vehicle )

    def __str__(self):
            return "ID_kierowcy = " + self.ID_kierowcy.__str__() + \
                   "Nr_rej = " + self.Nr_rej.__str__()


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


