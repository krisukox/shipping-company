from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Account,Employee,Address,Customer,Driver,Service,OrdersHistory,Vehicle,Timetable,Drivers_Vehicles
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.contrib.auth.forms import UserCreationForm
from .forms import UpdateAccountForm, RegisterForm, DriverRegisterForm, EmployeeRegisterForm
from .models import add_account, check_account, add_customer, add_driver, add_employee

from django.shortcuts import get_object_or_404
from django.contrib.auth import views as pom_view



class TimetableCreate(CreateView):
    info_sended = False
    model = Timetable
    fields = '__all__'

class TimetableDelete(DeleteView):
    model = Timetable
    success_url = reverse_lazy('timetables')


class TimetableUpdate(UpdateView):
    model = Timetable
    fields = ['data_pocz', 'data_kon','driver','service']

class OrdersHistoryCreate(CreateView):
    info_sended = False
    model = OrdersHistory
    fields = '__all__'

class OrdersHistoryDelete(DeleteView):
    model = OrdersHistory
    success_url = reverse_lazy('orderhistories')


class OrdersHistoryUpdate(UpdateView):
    model = OrdersHistory
    fields = ['account', 'service','startAddress','endAddress']

class AccountCreate(CreateView):
    info_sended = False
    model = Account
    fields = '__all__'


def create(request):
    if request.user.is_staff:
        view_function = AccountCreate.as_view()
        return view_function(request)
    return HttpResponse("<h1>Permission Denied</h1>")


def login(request):
    # return HttpResponse("<h1>Juz jestes zalogowany</h1>")
    if not request.user.is_authenticated:
        view_function = pom_view.LoginView.as_view(template_name='login.html')
        return view_function(request)
    return profile(request)


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


def driver_register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = DriverRegisterForm(request.POST)
            if form.is_valid():
                doswiadczenie = form.cleaned_data['doswiadczenie']
                kat_prawa_jazdy = form.cleaned_data['kat_prawa_jazdy']

                add_driver(password=form.cleaned_data['password1'],
                           username=form.cleaned_data['username'],
                           doswiadczenie=doswiadczenie,
                           kat_prawa_jazdy = kat_prawa_jazdy)

                return render(request, 'registration/success_register.html')
            else:
                print("blad")
        form = DriverRegisterForm()
        args = {'form': form}
        return render(request, 'registration/register.html', args)
    return HttpResponse("<h1>You are logged already</h1>")


def employee_register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = EmployeeRegisterForm(request.POST)
            if form.is_valid():
                add_employee(password=form.cleaned_data['password1'],
                           username=form.cleaned_data['username'],
                           stanowisko=form.cleaned_data['stanowisko'])

                return render(request, 'registration/success_register.html')
            else:
                print("blad")
        form = EmployeeRegisterForm()
        args = {'form': form}
        return render(request, 'registration/register.html', args)
    return HttpResponse("<h1>You are logged already</h1>")


def register(request):
    if not request.user.is_authenticated:
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
    return HttpResponse("<h1>You are logged already</h1>")


def profile(request):
    args = {'user': request.user}
    if request.user.is_staff:
        return render(request, 'profile/profile_admin.html', args)
    account_type = check_account(request.user)
    if account_type:
        if account_type == 'customer':
            return render(request, 'profile/profile_customer.html', args)
        if account_type == 'employee':
            return render(request, 'profile/profile_employee.html', args)
        if account_type == 'driver':
            return render(request, 'profile/profile_driver.html', args)
    else:
        return render(request, 'registration/login.html', args)


def edit_timetable(request):
    return HttpResponse("<h1>edit timetable</h1>")


def edit_timetable_all(request):
    return HttpResponse("<h1>edit timetable all</h1>")
# def new_account(request):
#     if request.user.is_staff:



def loginhome(request):
    return HttpResponseRedirect('/account/login/')


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


