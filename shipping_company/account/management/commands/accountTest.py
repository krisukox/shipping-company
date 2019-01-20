from django.core.management.base import BaseCommand
from account.models import Account, Address, Employee, Customer
from account.models import add_account, delete_account, check_account
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Simple database test'

    def display(self, objects):
        for x in objects.all():
            print(x)

    def handle(self, *args, **kwargs):
        delete_account()

        add_account(PESEL = 123, username='user1', password='pass')
        # add_account(imie='Jan', username='user2', password='pass')
        # add_account(nazwisko='Kowalski', username='user3', password='pass')

        check_account(username='user1')

        print("\n"+"ACCOUNTS -> ")
        self.display(Account.objects)

        delete_account(PESEL = 123)
        # delete_account(imie='Jan')
        # delete_account(nazwisko='Kowalski')

        print("\n"+"ACCOUNTS -> ")
        self.display(Account.objects)