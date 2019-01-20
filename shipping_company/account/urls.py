from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from. import views
from django.contrib.auth import views as pom_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('accounts/',views.AccountListView.as_view(), name='accounts'),
    path('employees/',views.EmployeeListView.as_view(), name='employees'),
    path('addresses/', views.AddressListView.as_view(),name='addresses'),
    path('customers/',views.CustomerListView.as_view(),name='customers'),
    path('drivers/',views.DriverListView.as_view(),name='drivers'),
    path('services/',views.ServiceListView.as_view(),name='services'),
    path('orderhistories/',views.OrdersHistoryListView.as_view(),name='orderhistories'),
    path('timetables/',views.TimetableListView.as_view(),name='timetables'),
    path('vehicles/',views.VehicleListView.as_view(),name='vehicles'),
    path('driversvehicles/',views.Drivers_VehiclesListView.as_view(),name='driversvehicles'),
    # url(r'^login/', pom_view.LoginView.as_view(template_name='login.html')),
    url(r'^register/', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile')
]
