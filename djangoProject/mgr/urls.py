from django.urls import path
# from mgr import customer
from mgr import sign_in_out
# from mgr import medicine
from mgr.views import listorders

from . import views

urlpatterns = [
    path('', views.listorders,name="home"),
    path('orders', listorders),
    # path('customers', customer.dispatcher),
    # path('medicines', medicine.dispatcher),
    path('signin', sign_in_out.signin),
    path('signout', sign_in_out.signout),
]
