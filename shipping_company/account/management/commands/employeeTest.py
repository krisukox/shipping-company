from django.core.management.base import BaseCommand
from account.models import Account, Address, Employee, Customer
from account.models import add_account, delete_account, add_employee, delete_employee, delete_employee_with_account, get_account_id

class Command(BaseCommand):
    help = 'Simple database test'

    def display(self, objects):
        for x in objects.all():
            print(x)

    def handle(self, *args, **kwargs):
        add_account(imie='Jan', nazwisko='Kowalski', PESEL=123)
        add_account(imie='Tomasz', nazwisko='Nowak', PESEL=125)

        add_employee(imie='Jan', nazwisko='Kowalski', stanowisko = 'sprzedawca')
        add_employee(imie='Tomasz', nazwisko='Nowak', stanowisko = 'kierownik')
        add_employee(stanowisko='manager')

        print("\n"+"ACCOUNTS -> ")
        self.display(Account.objects)
        print("EMPLOYEES -> ")
        self.display(Employee.objects)

        delete_employee_with_account(stanowisko='manager')

        print("\n"+"ACCOUNTS -> ")
        self.display(Account.objects)
        print("EMPLOYEES -> ")
        self.display(Employee.objects)

        delete_account(nazwisko='Nowak')

        print("\n"+"ACCOUNTS -> ")
        self.display(Account.objects)
        print("EMPLOYEES -> ")
        self. display(Employee.objects)

        delete_employee(nazwisko='Kowalski')

        print("\n"+"ACCOUNTS -> ")
        self.display(Account.objects)
        print("EMPLOYEES -> ")
        self. display(Employee.objects)

        delete_account(nazwisko='Kowalski')

        print("\n" + "ACCOUNTS -> ")
        self.display(Account.objects)
        print("EMPLOYEES -> ")
        self.display(Employee.objects)