from django.urls import path
from mgr import customer, sign_in_out, medicine

urlpatterns = [

    path('customers', customer.dispatcher),
    path('medicines', medicine.dispatcher),
    path('signin', sign_in_out.signin),
    path('signout', sign_in_out.signout),
]
