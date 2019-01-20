from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from. import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('accounts/',views.AccountListView.as_view(), name='accounts'),
    path('accounts/<int:pk>', views.AccountDetailView.as_view(), name='account-detail'),
    path('employees/',views.EmployeeListView.as_view(), name='employees'),
    path('addresses/', views.AddressListView.as_view(),name='addresses'),
    path('customers/',views.CustomerListView.as_view(),name='customers'),
    path('drivers/',views.DriverListView.as_view(),name='drivers'),
    path('services/',views.ServiceListView.as_view(),name='services'),
    path('orderhistories/',views.OrdersHistoryListView.as_view(),name='orderhistories'),
    path('timetables/',views.TimetableListView.as_view(),name='timetables'),
    path('vehicles/',views.VehicleListView.as_view(),name='vehicles'),
    path('driversvehicles/',views.Drivers_VehiclesListView.as_view(),name='driversvehicles'),
    path('create/', views.AccountCreate.as_view(), name='account_create'),
    path('account/<int:pk>/delete/', views.AccountDelete.as_view(), name='account_delete'),
    path('account/<int:pk>/update/', views.AccountUpdate.as_view(), name='account_update'),

]
