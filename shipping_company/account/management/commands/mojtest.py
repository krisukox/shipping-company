from django.core.management.base import BaseCommand
from account.models import Account, Address, Employee, Customer


class Command(BaseCommand):
    help = 'Simple database test'

    def display(self, objects):
        for x in objects.all():
            print(x)

    def handle(self, *args, **kwargs):
        Account.objects.filter(PESEL=12345678901).delete()
        Account.objects.filter(imie="Krzysztof").delete()

        print("\n" + "Dodanie dwoch kont oraz dwoch pracownikow")

        Account(PESEL=12345678901).save()
        Account(imie="Krzysztof").save()
        Employee(account=Account.objects.get(PESEL=12345678901), stanowisko="pomocnik").save()
        Employee(account=Account.objects.get(imie="Krzysztof"), stanowisko="kierownik").save()

        # self.display(Account.objects)

        print("\n"+"ACCOUNTS -> ")
        self.display(Account.objects)
        print("EMPLOYEES -> ")
        self.display(Employee.objects)

        print("\n" + "Usuniecie pracownika na stanowisku 'kierownik'")

        Employee.objects.filter(stanowisko="kierownik").delete()

        print("\n" + "ACCOUNTS -> ")
        self.display(Account.objects)
        print("EMPLOYEES -> ")
        self.display(Employee.objects)

        print("\n" + "Usuniecie konta z peselem 12345678901")

        Account.objects.filter(PESEL=12345678901).delete()

        print("\n" + "ACCOUNTS -> ")
        self.display(Account.objects)
        print("EMPLOYEES -> ")
        self.display(Employee.objects)

        print("\n" + "Usuniecie konta z imieniem 'Krzysztof'")

        Account.objects.filter(imie="Krzysztof").delete()

        print("\n" + "ACCOUNTS -> ")
        self.display(Account.objects)
        print("EMPLOYEES -> ")
        self.display(Employee.objects)
