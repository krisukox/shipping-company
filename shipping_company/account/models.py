from django.db import models
from django.urls import reverse
import datetime
from django.db.models.signals import post_save
from django.contrib.auth.models import User, UserManager
from django.contrib.auth import get_user, get_user_model


class Account(models.Model):
    ID_konta = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    PESEL = models.IntegerField(null=True)
    imie = models.CharField(max_length=40, blank=True)
    nazwisko = models.CharField(max_length=40, blank=True)
    data_zalozenia_konta = models.DateField(("Date"), default=datetime.date.today)

    def delete(self, *args, **kwargs):
        self.user.delete()
        # return super(self.__class__, self).delete(*args, **kwargs)

    def __str__(self):
        return "ID konta = " + self.ID_konta.__str__() + '\n' + \
               ", PESEL = " + self.PESEL.__str__()+ '\n' + \
               ", Imie = " + self.imie.__str__() + '\n' + \
               ", Nazwisko = " + self.nazwisko.__str__() + '\n' + \
               ", Data zalozenia konta = " + self.data_zalozenia_konta.__str__() + '\n'

    def get_absolute_url(self):

        return reverse('account-detail', args=[str(self.id)])




class Employee(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    stanowisko = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return "ID konta = " + self.account_id.__str__() + '\n' + \
               ", stanowisko = " + self.stanowisko.__str__() + '\n'

    def get_absolute_url(self):
        return reverse('employee-detail', args=[str(self.id)])

class Address(models.Model):
    ID_adresu = models.AutoField(primary_key=True)
    miasto = models.CharField(max_length=50, blank=True)
    kod_pocztowy = models.IntegerField(null=True)
    ulica = models.CharField(max_length=50, blank=True)
    nr_budynku = models.IntegerField(null=True)
    nr_lokalu = models.IntegerField(null=True)

    def __str__(self):
        return "ID_adresu = " + self.ID_adresu.__str__() + '\n' + \
               ", Miasto = " + self.miasto.__str__() + '\n' + \
               ", kod pocztowy = " + self.kod_pocztowy.__str__() + '\n' + \
               ", Ulica = " + self.ulica.__str__() + '\n' + \
               ", Numer budynku = " + self.nr_budynku.__str__() + '\n' + \
               ", Numer lokalu = " + self.nr_lokalu.__str__() + '\n'

    def get_absolute_url(self):
        return reverse('address-detail', args=[str(self.id)])

class Customer(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)
    NIP = models.IntegerField(blank=True)

    def __str__(self):
        return "ID_konta = " + self.account_id.__str__() + '\n' + \
               ", ID_adresu = " + self.address_id.__str__() + '\n' + \
               ", NIP = " + self.NIP.__str__() + '\n'

    def get_absolute_url(self):
        return reverse('customer-detail', args=[str(self.id)])

#
# def create_customer_profile(sender, **kwargs):
#     if kwargs['created']:
#         customer_profile = Customer.objects.create(user)


# post_save.connect(create_customer_profile, sender=Customer)


class Driver(models.Model):
    ID_kierowcy = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    kat_prawa_jazdy = models.CharField(max_length=20, blank=False, null=False,default=0)
    doswiadczenie = models.IntegerField(null=False,default=0)

    def __str__(self):
        return "ID_kierowcy = " + self.ID_kierowcy.__str__() + '\n' + \
               " ,ID_konta = " + self.account.__str__() + '\n' + \
               " ,Kat prawa jazdy " + self.kat_prawa_jazdy.__str__() + '\n' + \
               " ,Dowswiadczenie " + self.doswiadczenie.__str__() + '\n'

    def get_absolute_url(self):
        return reverse('driver-detail', args=[str(self.id)])

class Service(models.Model):
    ID_uslugi = models.AutoField(primary_key = True)
    opis_uslugi = models.CharField(max_length = 100, blank=False, null=False)
    koszt = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return "ID_uslugi = " + self.ID_uslugi.__str__() + '\n' + \
               "opis_uslugi = " + self.opis_uslugi.__str__() + '\n' + \
               "koszt " + self.koszt.__str__() + '\n'

    def get_absolute_url(self):
        return reverse('service-detail', args=[str(self.id)])

class OrdersHistory(models.Model):
    ID_zamowienia = models.AutoField(primary_key = True)
    account = models.OneToOneField(Account, on_delete = models.SET_NULL, blank=False,null=True)
    service = models.OneToOneField(Service , on_delete = models.SET_NULL, blank=False, null=True)
    startAddress = models.OneToOneField(Address , on_delete = models.SET_NULL, related_name="startAddress",blank=False, null=True)
    endAddress = models.OneToOneField(Address, on_delete = models.SET_NULL,related_name="endAddress" ,blank=False, null=True)

    def __str__(self):
        return "ID_zamowienia = " + self.ID_zamowienia.__str__() + '\n' + \
               "ID_konta = " + self.account_id.__str__() +  '\n' + \
               "ID_uslugi = " + self.service_id.__str__() + '\n' + \
               "ID_adresu_pocz = " + self.startAddress_id.__str__() + '\n' + \
               "ID_adresu_kon = " + self.endAddress_id.__str__() + '\n'

    def get_absolute_url(self):
        return reverse('ordershistory-detail', args=[str(self.id)])

class Vehicle(models.Model):
    Nr_rej = models.CharField(max_length = 20, primary_key = True)
    marka = models.CharField(max_length = 40, blank=True,null=True)
    model = models.CharField(max_length=40, blank=True, null=True)
    atrybut = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
            return "Nr_rej = " + self.Nr_rej.__str__() + '\n' + \
                   ", marka = " + self.marka.__str__() + '\n' + \
                   ", model =  " + self.model.__str__() + '\n' + \
                   ", atrybut = " + self.atrybut.__str__() + '\n'

    def get_absolute_url(self):
        return reverse('vehicle-detail', args=[str(self.id)])

class Timetable(models.Model):
    ID_terminu = models.AutoField(primary_key = True)
    data_pocz = models.DateField(blank = False, null=False)
    data_kon = models.DateField(blank = False, null=False)
    driver = models.ForeignKey(Driver, on_delete = models.SET_NULL, blank = False, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, blank=False, null=True)

    def __str__(self):
            return "ID_terminu = " + self.ID_terminu.__str__() + '\n' + \
                   "data_pocz = " + self.data_pocz.__str__() + '\n' + \
                   "data_kon " + self.data_kon.__str__() + '\n' + \
                   "ID_kierowcy " + self.driver_id.__str__() + '\n' + \
                    "ID_zamowienia " + self.service_id.__str__() + '\n'

    def get_absolute_url(self):
        return reverse('timetable-detail', args=[str(self.id)])

class Drivers_Vehicles(models.Model):
    kierowca = models.OneToOneField(Driver, on_delete=models.CASCADE, null=True)
    pojazd = models.OneToOneField(Vehicle, on_delete=models.CASCADE, null=True)

    def __str__(self):
            return "kierowca = " + self.kierowca.__str__() + \
                   "\npojazd = " + self.pojazd.__str__()

    def get_absolute_url(self):
        return reverse('drivers_vehicles-detail', args=[str(self.id)])

# Metody do account


def add_account(PESEL=None, imie='', nazwisko='', username='', password=''):
    if PESEL and Account.objects.filter(PESEL=PESEL):
        return 'add account failed'
    if username and password:
        user = User.objects.create_user(username=username, password=password)
        account = Account(PESEL=PESEL, imie=imie, nazwisko=nazwisko, user=user)
        account.save()
        return account
    return False


def check_account(username=''):
    resultUser = User.objects.all()
    if username:
        resultUser = resultUser.filter(username=username)
        print(resultUser.count())
        if resultUser.count() == 1:
            user = resultUser[0]
            account = Account.objects.get(user=user)
            # print(account.__str__())
            print(account.ID_konta)
            if Employee.objects.all().filter(account_id=account.ID_konta):
                return 'employee'
            if Customer.objects.all().filter(account_id=account.ID_konta):
                return 'customer'
            if Driver.objects.all().filter(account_id=account.ID_konta):
                return 'driver'
        else:
            return False

    else:
        return False


def delete_account(PESEL = None, imie = '', nazwisko = '', username = ''):
    result = Account.objects.all()
    resultUser = User.objects.all()
    if username:
        resultUser.filter(username=username)

        return
    if PESEL:
        result = result.filter(PESEL=PESEL)
    if imie:
        result = result.filter(imie=imie)
    if nazwisko:
        result = result.filter(nazwisko=nazwisko)
    for res in result:
        res.delete()


def get_account_id(imie,nazwisko):
    return Account.objects.filter(imie=imie, nazwisko=nazwisko).values("ID_konta")

# Metody do Employee


def add_employee(stanowisko, pesel = None, imie = '', nazwisko = '', username='', password=''):
    account = add_account(PESEL=pesel, imie=imie, nazwisko=nazwisko, username=username, password=password)
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
                 nr_budynku=None,
                 username='',
                 password=''):
    account = add_account(PESEL=pesel,imie=imie,nazwisko=nazwisko, username=username, password=password)
    if isinstance(account, Account):
        print("JEEEEEST")
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


def add_driver(kat_prawa_jazdy, doswiadczenie, pesel = None, imie = '', nazwisko = '', username='', password=''):
    account = add_account(PESEL=pesel, imie=imie, nazwisko=nazwisko, username=username, password=password)
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
        opis_uslugi=opis_uslugi,
        koszt=koszt)
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

def get_service_id(opis_uslugi='',koszt=''):
    return Account.objects.filter(opis_uslugi=opis_uslugi, koszt=koszt).values("ID_uslugi")

# Metody do Timetable


def add_timetable(data_pocz=datetime.date.today(),data_kon=datetime.date.today(),
                  pesel=None,imie='',nazwisko='',
                  kat_prawa_jazdy='C', doswiadczenie=10,
                  opis_uslugi='',koszt=None):
    driver = add_driver(pesel=pesel,imie=imie,nazwisko=nazwisko, kat_prawa_jazdy=kat_prawa_jazdy,doswiadczenie=doswiadczenie)
    service = add_service(opis_uslugi=opis_uslugi,koszt=koszt)
    if isinstance(driver, Driver):
        if isinstance(service, Service):
            timetable = Timetable(data_pocz=data_pocz, data_kon=data_kon, driver=driver,service=service)
            timetable.save()
            return timetable
    return 'Add timetable failed'

def delete_timetable(data_pocz=datetime.date.today(),data_kon=datetime.date.today(),
                     pesel=None, imie='', nazwisko='',
                     kat_prawa_jazdy='C', doswiadczenie=10,
                     opis_uslugi='', koszt=None):
    result = Timetable.objects.all()
    if data_pocz:
        result = result.filter(data_pocz=data_pocz)
    if data_kon:
        result = result.filter(data_kon=data_kon)
    timetable_for_delete = result
    result = Timetable.objects.all()
    result = result.values('service_id')
    result = Service.objects.filter(ID_uslugi__in=result)
    if opis_uslugi:
        result = result.filter(opis_uslugi=opis_uslugi)
    if koszt:
        result = result.filter(koszt=koszt)
    result = Service.objects.all()
    service_for_delete = result

    result = Timetable.objects.all()
    result = result.values('driver_id')
    result = Driver.objects.filter(ID_kierowcy__in=result)
    if kat_prawa_jazdy:
        result = result.filter(kat_prawa_jazdy=kat_prawa_jazdy)
    if doswiadczenie:
        result = result.filter(doswiadczenie=doswiadczenie)
    driver_for_delete = result


    driver_for_delete.delete()
    service_for_delete.delete()
    timetable_for_delete.delete()

# Metody do Order

def add_order(pesel=None,imie='',nazwisko='',
              opis_uslugi='',koszt=None,
              miasto='', kod_pocztowy=None, ulica='', nr_lokalu=None, nr_budynku=None):
    account = add_account(PESEL=pesel, imie=imie, nazwisko=nazwisko)
    service = add_service(opis_uslugi=opis_uslugi, koszt=koszt)
    address = add_address(miasto=miasto,kod_pocztowy=kod_pocztowy,ulica=ulica,nr_lokalu=nr_lokalu,nr_budynku=nr_budynku)
    if isinstance(account, Account):
        if isinstance(service, Service):
            if isinstance(address,Address):
                    order =OrdersHistory(account=account,service=service,startAddress=address,endAddress=address)
                    order.save()
                    return order
    return 'Add order failed'

def delete_order(pesel=None, imie='',nazwisko='',
                 opis_uslugi='', koszt=None,
                 miasto='', kod_pocztowy=None, ulica='', nr_lokalu=None, nr_budynku=None):
    result = OrdersHistory.objects.all()
    result = result.values('account_id')
    result = Account.objects.filter(ID_konta__in=result)
    if pesel:
        result = result.filter(PESEL=pesel)
    if imie:
        result = result.filter(imie=imie)
    if nazwisko:
        result = result.filter(nazwisko=nazwisko)
    account_for_delete = result

    result = OrdersHistory.objects.all()
    result = result.values('service_id')
    result = Service.objects.filter(ID_uslugi__in=result)
    if opis_uslugi:
        result = result.filter(opis_uslugi=opis_uslugi)
    if koszt:
        result = result.filter(koszt=koszt)
    service_for_delete = result

    result = OrdersHistory.objects.all()
    result = result.values('startAddress_id')
    result = Address.objects.filter(ID_adresu__in=result)
    if miasto:
        result = result.filter(miasto=miasto)
    if kod_pocztowy:
        result = result.filter(kod_pocztowy=kod_pocztowy)
    if ulica:
        result = result.filter(ulica=ulica)
    if nr_lokalu:
        result = result.filter(nr_lokalu=nr_lokalu)
    if koszt:
        result = result.filter(nr_budynku=nr_budynku)
    address_for_delete = result

    result=OrdersHistory.objects.all()
    result = result.values('ID_zamowienia')
    result = OrdersHistory.objects.filter(ID_zamowienia__in=result)
    order_to_delete = result

    order_to_delete.delete()
    address_for_delete.delete()
    service_for_delete.delete()
    account_for_delete.delete()


#def delete_customer(nip=None, pesel = None, imie = '', nazwisko = ''):
#    result = Customer.objects.all()
 #   if nip:
#        result = result.filter(NIP=nip)

#
 #   result = result.values('account_id')
  #  result = Account.objects.filter(ID_konta__in=result)
   # if pesel:
  #      result = result.filter(PESEL=pesel)
 #   if imie:
 #       result = result.filter(imie=imie)
 #   if nazwisko:
 #       result = result.filter(nazwisko=nazwisko)
 #   account_for_delete = result
 #   result = result.values('ID_konta')
 #   result = Customer.objects.filter(account_id__in=result)
#    result = result.values('address_id')
 #   address_for_delete = Address.objects.filter(ID_adresu__in=result)
  #  address_for_delete.delete()
  #  account_for_delete.delete()

#class OrdersHistory(models.Model):
 #   ID_zamowienia = models.AutoField(primary_key = True)
  #  account = models.ForeignKey(Account, on_delete = models.SET_NULL, blank=False,null=True)
   # service = models.ForeignKey(Service , on_delete = models.SET_NULL, blank=False, null=True)
    #startAddress = models.ForeignKey(Address , on_delete = models.SET_NULL, related_name="ID_adresu_pocz",blank=False, null=True)
    #endAddress = models.ForeignKey(Address, on_delete = models.SET_NULL,related_name="ID_adresu_kon" ,blank=False, null=True)
