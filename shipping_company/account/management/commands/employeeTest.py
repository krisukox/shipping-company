from django.core.management.base import BaseCommand
from account.models import Account, Address, Employee, Customer
from account.models import add_account, delete_account, get_account_id

class Command(BaseCommand):
    help = 'Simple database test'

    def display(self, objects):
        for x in objects.all():
            print(x)

    def handle(self, *args, **kwargs):
        add_account(imie='Jan', nazwisko='Kowalski', PESEL=123)
        add_account(imie='Jan', nazwisko='Kowalski', PESEL=123)


        print("\n"+"ACCOUNTS -> ")
        self.display(Account.objects)
        # print("EMPLOYEES -> ")
        # self.display(Employee.objects)

        print(get_account_id('Jan', 'Kowalski'))
        # print(Account.objects.filter(imie='Jan', nazwisko='Kowalski'))

        delete_account(imie='Jan')

        print("\n"+"ACCOUNTS -> ")
        self.display(Account.objects)
        # print("EMPLOYEES -> ")
        # self. display(Employee.objects)