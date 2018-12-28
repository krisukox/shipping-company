from django.http import HttpResponse
from django.shortcuts import render
from .models import Account,Employee,Address,Customer,Driver,Service,OrdersHistory,Vehicle,Timetable,Drivers_Vehicles
from django.views import generic

class AccountListView(generic.ListView):
    model = Account

class EmployeeListView(generic.ListView):
    model = Employee

class AddressListView(generic.ListView):
    model = Address

class CustomerListView(generic.ListView):
    model = Customer


class DriverListView(generic.ListView):
    model = Driver


class ServiceListView(generic.ListView):
    model = Service


class OrdersHistoryListView(generic.ListView):
    model = OrdersHistory


class TimetableListView(generic.ListView):
    model = Timetable

class VehicleListView(generic.ListView):
    model = Vehicle

class Drivers_VehiclesListView(generic.ListView):
    model = Drivers_Vehicles

def home(request):

    num_accounts = Account.objects.all().count()
    num_employees= Employee.objects.all().count()
    num_addresses = Address.objects.all().count()
    num_customers = Customer.objects.all().count()
    num_drivers = Driver.objects.all().count()
    num_services = Service.objects.all().count()
    num_order = OrdersHistory.objects.all().count()
    num_timetables= Timetable.objects.all().count()
    num_vehicles = Vehicle.objects.all().count()
    num_drivers_vehicles = Drivers_Vehicles.objects.all().count()

    context = {
        'num_accounts': num_accounts,
        'num_employees': num_employees,
        'num_addresses': num_addresses,
        'num_customers': num_customers,
        'num_drivers': num_drivers,
        'num_services': num_services,
        'num_order': num_order,
        'num_timetables': num_timetables,
        'num_vehicles': num_vehicles,
        'num_drivers_vehicles': num_drivers_vehicles
    }

    return render(request,'home.html',context=context)


