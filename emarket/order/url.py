from  django.urls import path
from . import views

app_name = "order"
urlpatterns = [
    path('orders/new',views.new_order, name ='orders'),
    path('orders/show/',views.get_orders, name ='orders'),
    path('orders/show/<int:pk>',views.get_order, name ='orders'),

]