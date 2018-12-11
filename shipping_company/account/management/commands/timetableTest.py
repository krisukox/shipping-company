from django.core.management.base import BaseCommand
from account.models import Account, Address, Employee, Customer, OrdersHistory, Service, Timetable
from account.models import add_order, delete_order, add_account, add_timetable,delete_timetable


class Command(BaseCommand):
    help = 'Simple database test'

    def display(self, objects):
        for x in objects.all():
            print(x)

    def handle(self, *args, **kwargs):


        print("\n" + "TIMETABLE -> ")
        self.display(Timetable.objects)




        print("\n" + "TIMETABLE -> ")
        self.display(Timetable.objects)

