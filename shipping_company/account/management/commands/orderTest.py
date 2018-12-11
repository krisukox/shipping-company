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

        add_order(PESEL=123,opis_uslugi='12345',miasto='wroclaw',koszt=999)



        print("\n"+"ORDERS -> ")
        self.display(OrdersHistory.objects)

