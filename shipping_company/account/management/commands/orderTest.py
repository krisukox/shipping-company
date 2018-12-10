from django.core.management.base import BaseCommand
from account.models import Account, Address, Employee, Customer, OrdersHistory, Service
from account.models import add_order , delete_order, add_account

class Command(BaseCommand):
    help = 'Simple database test'

    def display(self, objects):
        for x in objects.all():
            print(x)

    def handle(self, *args, **kwargs):

        k1=add_account(PESEL=123)


        print("\n" + "ORDERS -> ")
        self.display(OrdersHistory.objects)

        add_order(ID_zamowienia=123)


        delete_order(ID_zamowienia=123)
       


        print("\n"+"ORDERS -> ")
        self.display(OrdersHistory.objects)

