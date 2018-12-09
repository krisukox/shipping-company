from django.core.management.base import BaseCommand
from account.models import datetime,Account,OrdersHistory ,Address, Employee, Customer,Driver,Drivers_Vehicles,Timetable,Service,Vehicle


class Command(BaseCommand):
    help = 'Simple database test'

    def display(self, objects):
        for x in objects.all():
            print(x)

    def handle(self, *args, **kwargs):
        Account.objects.filter(PESEL=12345678901).delete()
        Account.objects.filter(imie="Krzysztof").delete()
        Account.objects.filter(imie="Janusz").delete()
        Driver.objects.filter(ID_kierowcy=123).delete();
        Driver.objects.filter(ID_kierowcy=124).delete();
        Address.objects.filter(miasto="Wroclaw").delete();
        Address.objects.filter(miasto="Wroclaw2").delete();
        Service.objects.filter(koszt=999).delete();
        Vehicle.objects.filter(Nr_rej = "DW123").delete();
        Vehicle.objects.filter(Nr_rej="DW321").delete();
        OrdersHistory.objects.filter(ID_zamowienia =123).delete();
        Timetable.objects.filter(ID_terminu = 777).delete();
        Drivers_Vehicles.objects.filter(ID_kierowcy=123).delete();
        print("\n" + "Dodanie obiektow reprezentujacych kazda z tabel")

        a1=Account(PESEL=12345678901).save()
        a2=Account(imie="Krzysztof").save()
        a3 = Account(imie="Janusz").save()
        Employee(account=Account.objects.get(PESEL=12345678901), stanowisko="pomocnik").save()
        Employee(account=Account.objects.get(imie="Krzysztof"), stanowisko="kierownik").save()
        Address(ID_adresu=123,miasto="Wroclaw").save()
        Address(ID_adresu=124, miasto="Wroclaw2", ulica="Biaal").save()
        d1=Driver(account = Account.objects.get(imie="Krzysztof"),ID_kierowcy=123).save()
        d2=Driver(account=Account.objects.get(imie="Janusz"), ID_kierowcy=124).save()
        Service(koszt = 999).save()
        Service(koszt=1999).save()
        v1=Vehicle(Nr_rej = "DW123", marka="AUDI").save()
        v2=Vehicle(Nr_rej="DW321", marka="BMW").save()
        OrdersHistory(
        ID_zamowienia = 123,
        ID_konta = Account.objects.get(imie="Krzysztof"),
        ID_uslugi = Service.objects.get(koszt=999),
        ID_adresu_pocz = Address.objects.get(ID_adresu =123),
        ID_adresu_kon = Address.objects.get(ID_adresu=124)).save()
        OrdersHistory(
        ID_zamowienia=125,
        ID_konta=Account.objects.get(imie="Krzysztof"),
        ID_uslugi=Service.objects.get(koszt=999),
        ID_adresu_pocz=Address.objects.get(ID_adresu=123),
        ID_adresu_kon=Address.objects.get(ID_adresu=124)).save()
        Timetable(
        ID_terminu = 777,
        data_pocz =(datetime.date.today()),
        data_kon = (datetime.date.today())).save()
        Timetable(
        ID_terminu=778,
        data_pocz=(datetime.date.today()),
        data_kon=(datetime.date.today())).save()

        # self.display(Account.objects)

        print("\n"+"ACCOUNTS -> ")
        self.display(Account.objects)
        print("EMPLOYEES -> ")
        self.display(Employee.objects)
        print("\n" + "ADDRESS -> ")
        self.display(Address.objects)
        print("DRIVERS -> ")
        self.display(Driver.objects)
        print("\n" + "SERVICE -> ")
        self.display(Service.objects)
        print("VEHICLE -> ")
        self.display(Vehicle.objects)
        print("\n" + "OrdersHistory -> ")
        self.display(OrdersHistory.objects)
        print("Timetable -> ")
        self.display(Timetable.objects)

        print("\n" + "Usuniecie pracownika na stanowisku 'kierownik'")

        Employee.objects.filter(stanowisko="kierownik").delete()

        print("\n" + "ACCOUNTS -> ")
        self.display(Account.objects)
        print("EMPLOYEES -> ")
        self.display(Employee.objects)

        print("\n" + "Usuniecie konta z peselem 12345678901")

        Account.objects.filter(PESEL=12345678901).delete()

        print("\n" + "ACCOUNTS -> ")
        self.display(Account.objects)
        print("EMPLOYEES -> ")
        self.display(Employee.objects)

        print("\n" + "Usuniecie konta z imieniem 'Krzysztof'")

        Account.objects.filter(imie="Krzysztof").delete()

        print("\n" + "ACCOUNTS -> ")
        self.display(Account.objects)
        print("EMPLOYEES -> ")
        self.display(Employee.objects)

        print("\n" + "Usuniecie adresu o id 123")
        Address.objects.filter(ID_adresu=123).delete()
        self.display(Address.objects)

        print("\n" + "Usuniecie kierowcy o id 124")
        Driver.objects.filter(ID_kierowcy=124).delete()
        self.display(Driver.objects)

        print("\n" + "Usuniecie pojazdu o marce BMW")
        Vehicle.objects.filter(marka="BMW").delete()
        self.display(Vehicle.objects)

        print("\n" + "Usuniecie uslugi o koszcie 999")
        Service.objects.filter(koszt=999).delete()
        self.display(Service.objects)

        print("\n" + "Usuniecie zamowienia o id 123")
        OrdersHistory.objects.filter(ID_zamowienia = 123).delete()
        self.display(OrdersHistory.objects)

        print("\n" + "Usuniecie terminu o id 777")
        Timetable.objects.filter(ID_terminu=777).delete()
        self.display(Timetable.objects)


