from django.contrib import admin
from.models import Account
from.models import Employee
from.models import Address
from.models import Customer
from.models import Driver
from.models import Service
from.models import OrdersHistory
from.models import Timetable

# Register your models here.
admin.site.register(Account)
admin.site.register(Employee)
admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Service)
admin.site.register(OrdersHistory)
admin.site.register(Timetable)


