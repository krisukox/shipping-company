from django.core.management.base import BaseCommand
from account.models import Account, Address, Employee, Customer, OrdersHistory, Service
from account.models import add_service,delete_service


class Command(BaseCommand):
    help = 'Simple database test'

    def display(self, objects):
        for x in objects.all():
            print(x)

    def handle(self, *args, **kwargs):
        print("\n" + "Service -> ")
        self.display(Service.objects)

        add_service(opis_uslugi='12345',koszt=999)
        add_service(koszt=1999)
        add_service(opis_uslugi='000', koszt=222)

        print("\n" + "Service -> ")
        self.display(Service.objects)

        delete_service(opis_uslugi='12345', koszt=999)
        delete_service(koszt=1999)
        delete_service(opis_uslugi='000', koszt=222)
        print("\n" + "Service -> ")
        self.display(Service.objects)
