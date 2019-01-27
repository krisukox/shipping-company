from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from. import views
from django.contrib.auth import views as pom_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('',views.loginhome, name='home'),
    # path('login/',views.home, name='home'),
    # url('d/', views.login, name='log'),
    path('accounts/',views.AccountListView.as_view(), name='accounts'),
    path('accounts/<int:pk>', views.AccountDetailView.as_view(), name='account-detail'),
    path('employees/',views.EmployeeListView.as_view(), name='employees'),
    path('addresses/', views.AddressListView.as_view(),name='addresses'),
    path('customers/',views.CustomerListView.as_view(),name='customers'),
    path('drivers/',views.DriverListView.as_view(),name='drivers'),
    path('services/',views.ServiceListView.as_view(),name='services'),
    path('orderhistories/',views.OrdersHistoryListView.as_view(),name='orderhistories'),
    path('timetables/',views.TimetableListView.as_view(),name='timetables'),
    path('edit-timatable/',views.edit_timetable,name='edit_timetables'),
    path('edit-timatable-all/',views.edit_timetable_all,name='edit_timetables_all'),
    path('vehicles/',views.VehicleListView.as_view(),name='vehicles'),
    path('driversvehicles/',views.Drivers_VehiclesListView.as_view(),name='driversvehicles'),
    path('create/', views.create, name='account_create'),
    # path('addacc/', views.new_account, name='account_add'),
    path('account/<int:pk>/delete/', views.AccountDelete.as_view(), name='account_delete'),
    path('account/<int:pk>/update/', views.AccountUpdate.as_view(), name='account_update'),
    path('cos/', views.TimetableListView.as_view()),
    url(r'^login/', views.login),
    url(r'^driverregister/', views.driver_register, name='driver_register'),
    url(r'^employeeregister/', views.employee_register, name='employee_register'),
    url(r'^register/', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile')
]
