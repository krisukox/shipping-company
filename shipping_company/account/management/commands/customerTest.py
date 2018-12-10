from django.core.management.base import BaseCommand
from account.models import Account, Address, Employee, Customer
from account.models import delete_customer, add_customer, add_account, delete_account, add_address, delete_address, add_employee, delete_employee, get_account_id

class Command(BaseCommand):
    help = 'Simple database test'

    def display(self, objects):
        for x in objects.all():
            print(x)

    def handle(self, *args, **kwargs):
        delete_account()
        delete_address()
        add_customer(pesel=123, nip=333, miasto='Wroclaw', imie='Jan', nazwisko='Kowalski')

        print("\n"+"ACCOUNTS -> ")
        self.display(Account.objects)
        print("CUSTOMER -> ")
        self.display(Customer.objects)
        print("ADDRESS -> ")
        self.display(Address.objects)

        delete_customer(nip=333,pesel=123, imie='Jan')

        print("\n" + "ACCOUNTS -> ")
        self.display(Account.objects)
        print("CUSTOMER -> ")
        self.display(Customer.objects)
        print("ADDRESS -> ")
        self.display(Address.objects)
