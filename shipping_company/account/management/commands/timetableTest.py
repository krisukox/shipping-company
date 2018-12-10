from django.core.management.base import BaseCommand
from account.models import Account, Address, Employee, Customer, OrdersHistory, Service, Timetable
from account.models import add_order, delete_order, add_account, add_timetable,delete_timetable


class Command(BaseCommand):
    help = 'Simple database test'

    def display(self, objects):
        for x in objects.all():
            print(x)

    def handle(self, *args, **kwargs):
        k1 = add_account(PESEL=123)

        print("\n" + "TIMETABLE -> ")
        self.display(Timetable.objects)

        add_timetable(ID_terminu=123)

        delete_timetable(ID_terminu=123)

        print("\n" + "TIMETABLE -> ")
        self.display(Timetable.objects)

