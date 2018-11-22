from django.urls import path, include
from . import views

app_name = 'settings'
urlpatterns = [
    path('', views.setting_payment,name="settings_payment"),
    path('policy/', views.policy_payment,name="policy_payment"),
    path('payment/', views.payment_payment,name="payment_payment"),
]
