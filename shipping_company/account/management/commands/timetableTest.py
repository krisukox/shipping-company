from django.core.management.base import BaseCommand
from account.models import Account, Address, Employee, Customer, OrdersHistory, Service, Timetable
from account.models import add_order, delete_order, add_account, add_timetable,delete_timetable
import datetime

class Command(BaseCommand):
    help = 'Simple database test'

    def display(self, objects):
        for x in objects.all():
            print(x)

    def handle(self, *args, **kwargs):


        print("\n" + "TIMETABLE PRZED DODAWANIEM-> ")
        self.display(Timetable.objects)

        add_timetable(imie='Janusz', nazwisko='Siaki', opis_uslugi='Przewoz',
                      koszt=999,pesel=123, kat_prawa_jazdy='C', doswiadczenie=10,
                      data_pocz=datetime.date.today(), data_kon=datetime.date.today())
        add_timetable(imie='Siemens', nazwisko='Siaki', opis_uslugi='Przewoz',
                      koszt=999, pesel=456, kat_prawa_jazdy='C', doswiadczenie=10,
                      data_pocz=datetime.date.today(), data_kon=datetime.date.today())

        print("\n" + "TIMETABLE PO DODAWANIU-> ")
        self.display(Timetable.objects)

        delete_timetable(imie='Janusz', nazwisko='Taki', opis_uslugi='Przewoz', koszt=999,pesel=123, kat_prawa_jazdy='C', doswiadczenie=10, data_pocz=datetime.date.today(), data_kon=datetime.date.today())
        delete_timetable(imie='Siemens', nazwisko='Siaki', opis_uslugi='Przewoz', koszt=999, pesel=456, kat_prawa_jazdy='C', doswiadczenie=10, data_pocz=datetime.date.today(), data_kon=datetime.date.today())

        print("\n" + "TIMETABLE PO USUWANIU-> ")
        self.display(Timetable.objects)


        self.display(Timetable.objects)

