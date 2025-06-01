from django.contrib import admin
from django.urls import path
from . import views as v

#creat your urls here

app_name = 'piconverterapp'
urlpatterns = [
    path('' ,v.home ,name='homepage') ,
    path('pi-browser/', v.document, name='piconverter documentation') ,
    path('pi-wallet/', v.wallet, name='pi wallet'),
    path('walleterror/', v.exchange, name='wallet-error'),
    path('develop/', v.develop, name='pinet development'),
    path('pinet/pi-apps/community-development/', v.payment, name='payment place'),
    path('pi-payment/selection', v.pipay, name='pipayments'),
]