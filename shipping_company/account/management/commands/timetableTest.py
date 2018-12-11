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


        print("\n" + "TIMETABLE -> ")
        self.display(Timetable.objects)

        add_timetable(imie='Janusz', nazwisko='Siaki', opis_uslugi='Przewoz', koszt=999,
                      data_pocz=datetime.date.today(), data_kon=datetime.date.today())
        add_timetable(imie='Janusz2', nazwisko='Siaki', opis_uslugi='Przewoz3', koszt=333,
                      data_pocz=datetime.date.today(), data_kon=datetime.date.today())

        delete_timetable(imie='Janusz', nazwisko='Taki', opis_uslugi='Przewoz', koszt=999,
                     data_pocz=datetime.date.today(), data_kon=datetime.date.today())
        delete_timetable(imie='Janusz2', nazwisko='Siaki', opis_uslugi='Przewoz3', koszt=333,
                        data_pocz=datetime.date.today(), data_kon=datetime.date.today())



        self.display(Timetable.objects)

