from django.core.management.base import BaseCommand
from account.models import Account, Address, Employee, Customer
from account.models import add_account, delete_account, add_employee, delete_employee, get_account_id, check_account

class Command(BaseCommand):
    help = 'Simple database test'

    def display(self, objects):
        for x in objects.all():
            print(x)

    def handle(self, *args, **kwargs):
        add_employee(imie='Jan', nazwisko='Kowalski', stanowisko = 'sprzedawca', username='user4',
                     password='adminadmin')
        # add_employee(imie='Tomasz', nazwisko='Nowak', stanowisko = 'kierownik')
        # add_employee(stanowisko='manager')
        # print("dodanie poczatkowe konta oraz pracownik")
        print("\n"+"ACCOUNTS -> ")
        self.display(Account.objects)
        print("EMPLOYEES -> ")
        self.display(Employee.objects)

        check_account(username='user4')

        # delete_employee(stanowisko='manager')

        # print("\n"+"ACCOUNTS -> ")
        # self.display(Account.objects)
        # print("EMPLOYEES -> ")
        # self.display(Employee.objects)

        delete_account(nazwisko='Kowalski')

        # print("\n"+"ACCOUNTS -> ")
        # self.display(Account.objects)
        # print("EMPLOYEES -> ")
        # self. display(Employee.objects)

        # delete_employee(imie='Jan')

        print("\n"+"ACCOUNTS -> ")
        self.display(Account.objects)
        print("EMPLOYEES -> ")
        self. display(Employee.objects)