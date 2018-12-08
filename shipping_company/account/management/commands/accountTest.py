from django.core.management.base import BaseCommand
from account.models import Account, Address, Employee, Customer
from account.models import add_account, delete_account

class Command(BaseCommand):
    help = 'Simple database test'

    def display(self, objects):
        for x in objects.all():
            print(x)

    def handle(self, *args, **kwargs):
        add_account(PESEL = 123)
        add_account(imie='Jan')
        add_account(nazwisko='Kowalski')

        print("\n"+"ACCOUNTS -> ")
        self.display(Account.objects)

        delete_account(PESEL = 123)
        delete_account(imie='Jan')
        delete_account(nazwisko='Kowalski')

        print("\n"+"ACCOUNTS -> ")
        self.display(Account.objects)