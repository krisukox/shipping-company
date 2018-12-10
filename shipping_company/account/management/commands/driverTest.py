from django.core.management.base import BaseCommand
from account.models import Driver, Account, Vehicle, Drivers_Vehicles,\
                           add_driver, delete_driver, \
                           add_vehicle, delete_vehicle, add_vehicle_driver, delete_vehilce_driver

class Command(BaseCommand):
    help = 'Simple database test'

    def display(self, objects):
        for x in objects.all():
            print(x)

    def handle(self, *args, **kwargs):
        delete_vehilce_driver()
        add_driver(pesel=123, imie='Jan', nazwisko='Kowalski', kat_prawa_jazdy='C', doswiadczenie=10)
        add_vehicle(nr_rej='123asd', marka='scania')

        add_vehicle_driver(pesel=123)

        print("\n"+"ACCOUNTS -> ")
        self.display(Account.objects)
        print("DRIVER -> ")
        self.display(Driver.objects)
        print("VEHICLE -> ")
        self.display(Vehicle.objects)
        print("DRIVERS_VEHICLES -> ")
        self.display(Drivers_Vehicles.objects)

        delete_driver(pesel=123)
        delete_vehicle(marka='scania')

        print("\n"+"ACCOUNTS -> ")
        self.display(Account.objects)
        print("DRIVER -> ")
        self.display(Driver.objects)
        print("VEHICLE -> ")
        self.display(Vehicle.objects)
        print("DRIVERS_VEHICLES -> ")
        self.display(Drivers_Vehicles.objects)
