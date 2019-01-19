from django.core.management.base import BaseCommand
from account.models import Account, Address, Employee, Customer, OrdersHistory, Service
from account.models import add_order , delete_order, add_account

class Command(BaseCommand):
    help = 'Simple database test'

    def display(self, objects):
        for x in objects.all():
            print(x)

    def handle(self, *args, **kwargs):




        print("\n" + "ORDERS PRZED DODAWANIEM-> ")
        self.display(OrdersHistory.objects)

        add_order(pesel = 123,imie='Janusz', nazwisko='Taki',opis_uslugi='Przewoz',        koszt=999,miasto='Wroclaw', kod_pocztowy='123')
        add_order(pesel = 456,imie='Lukasz', nazwisko='Ja',  opis_uslugi='Przewoz towaru', koszt=100,miasto='Wroclaw', kod_pocztowy='12345')

        print("\n" + "ORDERS PO DODAWANIU-> ")
        self.display(OrdersHistory.objects)

        #delete_order(pesel = 123,imie='Janusz', nazwisko='Taki',opis_uslugi='Przewoz',koszt=999,miasto='Wroclaw',kod_pocztowy='123')
        #delete_order(pesel=456, imie='Lukasz', nazwisko='Ja', opis_uslugi='Przewoz towaru', koszt=100, miasto='Wroclaw', kod_pocztowy='12345')
        print("\n"+"ORDERS PO USUWANIU -> ")
        self.display(OrdersHistory.objects)

