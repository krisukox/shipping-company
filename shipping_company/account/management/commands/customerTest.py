from django.core.management.base import BaseCommand
from account.models import Account, Address, Employee, Customer
from account.models import delete_customer, add_customer, add_account, delete_account, add_address, delete_address, add_employee, delete_employee, delete_employee_with_account, get_account_id

class Command(BaseCommand):
    help = 'Simple database test'

    def display(self, objects):
        for x in objects.all():
            print(x)

    def handle(self, *args, **kwargs):
        delete_account()
        add_customer(pesel=123, nip=333)

        print("\n"+"ACCOUNTS -> ")
        self.display(Account.objects)
        print("CUSTOMER -> ")
        self.display(Customer.objects)

        delete_customer(pesel=123)

        print("\n" + "ACCOUNTS -> ")
        self.display(Account.objects)
        print("CUSTOMER -> ")
        self.display(Customer.objects)

        # add_account(imie='Jan', nazwisko='Kowalski', PESEL=123)
        # add_account(imie='Tomasz', nazwisko='Nowak', PESEL=125)
        #
        # add_address(miasto='Wroclaw')
        #
        # add_customer()
        #
        # print("\n" + "ADDRESS -> ")
        # self.display(Address.objects)
        #
        # delete_address(miasto='Wroclaw')
        #
        # print("\n" + "ADDRESS -> ")
        # self.display(Address.objects)
