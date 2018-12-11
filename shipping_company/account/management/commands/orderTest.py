from django.core.management.base import BaseCommand
from account.models import Account, Address, Employee, Customer, OrdersHistory, Service
from account.models import add_order , delete_order, add_account

class Command(BaseCommand):
    help = 'Simple database test'

    def display(self, objects):
        for x in objects.all():
            print(x)

    def handle(self, *args, **kwargs):




        print("\n" + "ORDERS -> ")
        self.display(OrdersHistory.objects)

        add_order(imie='Janusz',nazwisko='Taki',opis_uslugi='Przewoz',koszt=999,miasto='Wroclaw',kod_pocztowy='123')
        add_order(imie='Stefan', nazwisko='Siaki', opis_uslugi='Przewoz', koszt=9929, miasto='Warszawa', kod_pocztowy='567')

        delete_order(imie='Stefan', nazwisko='Siaki', opis_uslugi='Przewoz2', koszt=9929, miasto='Warszawa', kod_pocztowy='567')
        delete_order(imie='Janusz', nazwisko='Taki', opis_uslugi='Przewoz', koszt=999, miasto='Wroclaw',kod_pocztowy='123')

        print("\n"+"ORDERS -> ")
        self.display(OrdersHistory.objects)

