
from django.urls import path, include
from . import views
app_name = "cart"
urlpatterns = [
    path('', views.cart,name="cart"),
    path('<int:product_id>/', views.add_to_cart, name = 'add_to_cart'),
    path('<int:cart_id>/<str:dummy>/', views.remove_cart, name= 'remove_cart'),
]
