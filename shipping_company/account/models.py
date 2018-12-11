from django.db import models
import datetime


class Account(models.Model):
    ID_konta = models.AutoField(primary_key=True)
    PESEL = models.IntegerField(null=True)
    imie = models.CharField(max_length=40, blank=True)
    nazwisko = models.CharField(max_length=40, blank=True)
    data_zalozenia_konta = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return "ID konta = " + self.ID_konta.__str__() + \
               ", PESEL = " + self.PESEL.__str__() + \
               ", Imie = " + self.imie.__str__() + \
               ", Nazwisko = " + self.nazwisko.__str__() + \
               ", Data zalozenia konta = " + self.data_zalozenia_konta.__str__()


class Employee(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    stanowisko = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return "ID konta = " + self.account_id.__str__() + \
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
               " ,ID_konta = " + self.account.__str__() + \
               " ,Kat prawa jazdy " + self.kat_prawa_jazdy.__str__() + \
               " ,Dowswiadczenie " + self.doswiadczenie.__str__()


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
    account = models.ForeignKey(Account, on_delete = models.SET_NULL, blank=False,null=True)
    service = models.ForeignKey(Service , on_delete = models.SET_NULL, blank=False, null=True)
    startAddress = models.ForeignKey(Address , on_delete = models.SET_NULL, related_name="ID_adresu_pocz",blank=False, null=True)
    endAddress = models.ForeignKey(Address, on_delete = models.SET_NULL,related_name="ID_adresu_kon" ,blank=False, null=True)

    def __str__(self):
        return "ID_zamowienia = " + self.ID_zamowienia.__str__() + \
               "ID_konta = " + self.account.__str__() + \
               "Kat ID_uslugi jazdy " + self.service.__str__() + \
               "ID_adresu_pocz " + self.startAddress.__str__() + \
               "ID_adresu_kon " + self.endAddress.__str__()


class Vehicle(models.Model):
    Nr_rej = models.CharField(max_length = 20, primary_key = True)
    marka = models.CharField(max_length = 40, blank=True,null=True)
    model = models.CharField(max_length=40, blank=True, null=True)
    atrybut = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
            return "Nr_rej = " + self.Nr_rej.__str__() + \
                   ", marka = " + self.marka.__str__() + \
                   ", model =  " + self.model.__str__() + \
                   ", atrybut = " + self.atrybut.__str__()


class Timetable(models.Model):
    ID_terminu = models.AutoField(primary_key = True)
    data_pocz = models.DateField(blank = False, null=False)
    data_kon = models.DateField(blank = False, null=False)
    driver = models.ForeignKey(Driver, on_delete = models.SET_NULL, blank = False, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, blank=False, null=True)

    def __str__(self):
            return "ID_terminu = " + self.ID_terminu.__str__() + \
                   "data_pocz = " + self.data_pocz.__str__() + \
                   "data_kon " + self.data_kon.__str__() + \
                   "ID_kierowcy " + self.driver.__str__() + \
                    "ID_zamowienia " + self.service.__str__()


class Drivers_Vehicles(models.Model):
    kierowca = models.OneToOneField(Driver, on_delete=models.CASCADE, null=True)
    pojazd = models.OneToOneField(Vehicle, on_delete=models.CASCADE, null=True)

    def __str__(self):
            return "kierowca = " + self.kierowca.__str__() + \
                   "\npojazd = " + self.pojazd.__str__()



# Metody do account

def add_account(PESEL = None, imie = '', nazwisko = ''):
    if PESEL and Account.objects.filter(PESEL=PESEL):
        return 'add account failed'
    account = Account(PESEL=PESEL,imie = imie,nazwisko = nazwisko)
    account.save()
    return account


def delete_account(PESEL = None, imie = '', nazwisko = ''):
    result = Account.objects.all()

    if PESEL:
        result = result.filter(PESEL=PESEL)
    if imie:
        result = result.filter(imie=imie)
    if nazwisko:
        result = result.filter(nazwisko=nazwisko)

    result.delete()


def get_account_id(imie,nazwisko):
    return Account.objects.filter(imie=imie, nazwisko=nazwisko).values("ID_konta")

# Metody do Employee

def add_employee(stanowisko, pesel = None, imie = '', nazwisko = ''):
    account = add_account(PESEL=pesel, imie=imie, nazwisko=nazwisko)
    if isinstance(account, Account):
        employee = Employee(account=account, stanowisko=stanowisko)
        employee.save()
        return employee
    return 'add employee failed'


def delete_employee(stanowisko='', pesel = None, imie = '', nazwisko = ''):
    result = Employee.objects.all()
    if stanowisko:
        result = result.filter(stanowisko=stanowisko)
    result = result.values('account_id')
    result = Account.objects.filter(ID_konta__in=result)
    if pesel:
        result = result.filter(PESEL=pesel)
    if imie:
        result = result.filter(imie=imie)
    if nazwisko:
        result = result.filter(nazwisko=nazwisko)
    result.delete()


# Metody do Address

def add_address(miasto='', kod_pocztowy=None, ulica='', nr_lokalu=None, nr_budynku=None):
    address = Address(miasto=miasto,
                      kod_pocztowy=kod_pocztowy,
                      ulica=ulica,
                      nr_lokalu=nr_lokalu,
                      nr_budynku=nr_budynku)
    address.save()
    return address


def delete_address(miasto='', kod_pocztowy=None, ulica='', nr_lokalu=None, nr_budynku=None):
    result = Address.objects.all()
    if miasto:
        result = result.filter(miasto=miasto)
    if kod_pocztowy:
        result = result.filter(kod_pocztowy=kod_pocztowy)
    if ulica:
        result = result.filter(ulica=ulica)
    if nr_lokalu:
        result = result.filter(nr_lokalu=nr_lokalu)
    if nr_budynku:
        result = result.filter(nr_budynku=nr_budynku)

    result.delete()

# Metody do Customer

def add_customer(nip=None,
                 pesel = None,
                 imie = '',
                 nazwisko = '',
                 miasto='',
                 kod_pocztowy=None,
                 ulica='',
                 nr_lokalu=None,
                 nr_budynku=None):
    account = add_account(PESEL=pesel,imie=imie,nazwisko=nazwisko)
    if isinstance(account,Account):
        address = add_address(miasto=miasto,
                          kod_pocztowy=kod_pocztowy,
                          ulica=ulica,
                          nr_lokalu=nr_lokalu,
                          nr_budynku=nr_budynku)
        Customer(account=account, address=address, NIP=nip).save()


def delete_customer(nip=None, pesel = None, imie = '', nazwisko = ''):
    result = Customer.objects.all()
    if nip:
        result = result.filter(NIP=nip)

    result = result.values('account_id')
    result = Account.objects.filter(ID_konta__in=result)
    if pesel:
        result = result.filter(PESEL=pesel)
    if imie:
        result = result.filter(imie=imie)
    if nazwisko:
        result = result.filter(nazwisko=nazwisko)
    account_for_delete = result
    result = result.values('ID_konta')
    result = Customer.objects.filter(account_id__in=result)
    result = result.values('address_id')
    address_for_delete = Address.objects.filter(ID_adresu__in=result)
    address_for_delete.delete()
    account_for_delete.delete()

# Metody do Driver


def add_driver(kat_prawa_jazdy, doswiadczenie, pesel = None, imie = '', nazwisko = ''):
    account = add_account(PESEL=pesel, imie=imie, nazwisko=nazwisko)
    if isinstance(account, Account):
        driver = Driver(account=account, kat_prawa_jazdy=kat_prawa_jazdy, doswiadczenie=doswiadczenie)
        driver.save()
        return driver
    return 'add driver failed'


def delete_driver(pesel=None, imie='', nazwisko=''):
    result = Account.objects.all()
    if pesel:
        result = result.filter(PESEL=pesel)
    if imie:
        result = result.filter(imie=imie)
    if nazwisko:
        result = result.filter(nazwisko=nazwisko)
    result.delete()


# Metody do Vehicle


def add_vehicle(nr_rej, marka='', model='', atrybut=''):
    vehicle = Vehicle(Nr_rej=nr_rej, marka=marka, model=model, atrybut=atrybut)
    vehicle.save()
    return vehicle


def delete_vehicle(nr_rej='', marka='', model='', atrybut=''):
    if nr_rej:
        Vehicle.objects.filter(Nr_rej=nr_rej).delete()
        return
    result = Vehicle.objects.all()
    if marka:
        result = result.filter(marka=marka)
    if model:
        result = result.filter(model=model)
    if atrybut:
        result = result.filter(atrybut=atrybut)
    result.delete()


# Metody do Vehicle_Driver


def add_vehicle_driver(pesel=None, imie='', nazwisko='', nr_rej='', marka='', model=''):
    result = Account.objects.all()
    if pesel:
        result = result.filter(PESEL=pesel)
    if imie:
        result = result.filter(imie=imie)
    if nazwisko:
        result = result.filter(nazwisko=nazwisko)
    result = result.values('ID_konta')
    driver = Driver.objects.filter(account_id__in=result)

    result = Vehicle.objects.all()
    if nr_rej:
        result = result.filter(Nr_rej=nr_rej)
    if marka:
        result = result.filter(marka=marka)
    if model:
        result = result.filter(model=model)

    vehicle = result

    if driver.count() == 1 and vehicle.count() == 1:
        driver_vehicle = Drivers_Vehicles(kierowca=driver[0], pojazd=vehicle[0])
        driver_vehicle.save()
        # driver_vehicle.ID_kierowcy.add(driver[0])
        # Drivers_Vehicles(ID_kierowcy = driver, Nr_rej.set(vehicle))


def delete_vehilce_driver():
    result = Drivers_Vehicles.objects.all()
    result.delete()

# Metody do Service

def add_service(ID_uslugi=None,opis_uslugi='',koszt=None):
    service = Service(
        ID_uslugi=ID_uslugi,
        opis_uslugi=opis_uslugi
        ,koszt=koszt)
    service.save()
    return service

def delete_service(ID_uslugi=None,opis_uslugi='',koszt=None):
    result = Service.objects.all()
    if ID_uslugi:
        result = result.filter(ID_uslugi=ID_uslugi)
    if opis_uslugi:
        result = result.filter(opis_uslugi=opis_uslugi)
    if koszt:
        result = result.filter(koszt=koszt)
    result.delete()



# Metody do Timetable


def add_timetable(data_pocz=datetime.date.today(),data_kon=datetime.date.today(),
                  PESEL=None,imie='',nazwisko='',
                  opis_uslugi='',koszt=None):
    account = add_account(PESEL=PESEL, imie=imie, nazwisko=nazwisko)
    service = add_service(opis_uslugi=opis_uslugi,koszt=koszt)
    if isinstance(account, Account):
        if isinstance(service, Service):
            timetable = Timetable(data_pocz=data_pocz, data_kon=data_kon, account=account,service=service)
            timetable.save()
            return timetable
    return 'Add timetable failed'

def delete_timetable(data_pocz=datetime.date.today(),data_kon=datetime.date.today(),
                     PESEL=None,imie='',nazwisko='',
                     opis_uslugi='', koszt=None):
    result = Account.objects.all()
    if PESEL:
        result = result.filter(PESEL=PESEL)
    if imie:
        result = result.filter(imie=imie)
    if nazwisko:
        result = result.filter(nazwisko=nazwisko)
    result = Service.objects.all()
    if opis_uslugi:
        result = result.filter(opis_uslugi=opis_uslugi)
    if koszt:
        result = result.filter(koszt=koszt)
    result = Timetable.objects.all()
    if data_pocz:
        result = result.filter(data_pocz=data_pocz)
    if data_kon:
        result = result.filter(data_kon=data_kon)
    result.delete()


# Metody do Order

def add_order(PESEL=None,imie='',nazwisko='',
              opis_uslugi='',koszt=None,
              miasto='', kod_pocztowy=None, ulica='', nr_lokalu=None, nr_budynku=None):
    account = add_account(PESEL=PESEL, imie=imie, nazwisko=nazwisko)
    service = add_service(opis_uslugi=opis_uslugi, koszt=koszt)
    address = add_address(miasto=miasto,kod_pocztowy=kod_pocztowy,ulica=ulica,nr_lokalu=nr_lokalu,nr_budynku=nr_budynku)
    if isinstance(account, Account):
        if isinstance(service, Service):
            if isinstance(address,Address):
                    order =OrdersHistory(account=account,service=service,startAddress=address,endAddress=address)
                    order.save()
                    return order
    return 'Add order failed'

def delete_order(PESEL=None,imie='',nazwisko='',
                 opis_uslugi='', koszt=None,
                 miasto='', kod_pocztowy=None, ulica='', nr_lokalu=None, nr_budynku=None):
    result = Account.objects.all()
    if PESEL:
        result = result.filter(PESEL=PESEL)
    if imie:
        result = result.filter(imie=imie)
    if nazwisko:
        result = result.filter(nazwisko=nazwisko)
    result = Service.objects.all()
    if opis_uslugi:
        result = result.filter(opis_uslugi=opis_uslugi)
    if koszt:
        result = result.filter(koszt=koszt)
    result = Address.objects.all()
    if miasto:
        result = result.filter(miasto=miasto)
    if kod_pocztowy:
        result = result.filter(kod_pocztowy=kod_pocztowy)
    if ulica:
        result = result.filter(ulica=ulica)
    if nr_lokalu:
        result = result.filter(nr_lokalu=nr_lokalu)
    if nr_budynku:
        result = result.filter(nr_budynku=nr_budynku)
    result.delete()



