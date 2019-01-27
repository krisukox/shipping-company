from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Account,Employee,Address,Customer,Driver,Service,OrdersHistory,Vehicle,Timetable,Drivers_Vehicles
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.forms import UserCreationForm
from .forms import UpdateAccountForm, RegisterForm
from .models import add_account, check_account, add_customer

from django.shortcuts import get_object_or_404

class AccountCreate(CreateView):
    info_sended = False
    model = Account
    fields = '__all__'

class AccountDelete(DeleteView):
    model = Account
    success_url = reverse_lazy('accounts')

class AccountUpdate(UpdateView):
    model = Account
    fields = ['imie', 'nazwisko']

class AccountDetailView(generic.DetailView):
    model = Account

def account_detail_view(request, primary_key):
    account = get_object_or_404(Account, pk=primary_key)
    return render(request, 'account/account_detail.html', context={'account': account})

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


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            pesel = form.cleaned_data['PESEL']

            add_customer(pesel=pesel,
                         password=form.cleaned_data['password1'],
                         username=form.cleaned_data['username'])

            print(pesel)

            return render(request, 'registration/success_register.html')

    form = RegisterForm()
    args = {'form': form}
    return render(request, 'registration/register.html', args)


def profile(request):
    args = {'user': request.user}
    if request.user.is_staff:
        return render(request, 'registration/profile_admin.html', args)
    account_type = check_account(request.user)
    if account_type:
        if account_type == 'customer':
            return render(request, 'registration/profile_customer.html', args)
        if account_type == 'employee':
            return render(request, 'registration/profile_employee.html', args)
        if account_type == 'driver':
            return render(request, 'registration/profile_driver.html', args)
    else:
        return render(request, 'registration/login.html', args)

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

    return render(request, 'home.html', context=context)


