from django.core.management.base import BaseCommand
from account.models import datetime,Account,OrdersHistory ,Address, Employee, Customer,Driver,Drivers_Vehicles,Timetable,Service,Vehicle
from account.models import add_vehicle, add_account,add_address,add_customer,add_driver,add_employee,add_order,add_service,add_timetable


class Command(BaseCommand):
    help = 'Simple database test'

    def display(self, objects):
        for x in objects.all():
            print(x)

    def handle(self, *args, **kwargs):

        add_account(imie='Jan')
        add_address(miasto='Wroclaw')
        add_customer(pesel=123, nip=333, miasto='Wroclaw', imie='Jan', nazwisko='Kowalski')
        add_driver(pesel=253, imie='Jan', nazwisko='Kowalski', kat_prawa_jazdy='C', doswiadczenie=10)
        add_employee(imie='Tomasz', nazwisko='Nowak', stanowisko='kierownik')
        add_order(pesel=999, imie='Janusz', nazwisko='Taki', opis_uslugi='Przewoz', koszt=999, miasto='Wroclaw',
          kod_pocztowy='123')
        add_service(koszt=1999)
        add_timetable(imie='Janusz', nazwisko='Siaki', opis_uslugi='Przewoz',
                      koszt=999,pesel=413, kat_prawa_jazdy='C', doswiadczenie=10,
                      data_pocz=datetime.date.today(), data_kon=datetime.date.today())
        add_vehicle(nr_rej="DSW01S3", marka='BMW', model='E63', atrybut='')


