from django.urls import path, include
from . import views

app_name = 'checkout'

urlpatterns = [
    path('', views.checkout,name="checkout"),
    path('make_payment/', views.make_payment, name = 'make_payment'),



]
