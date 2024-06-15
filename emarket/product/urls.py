from django.urls import path
from . import views

urlpatterns = [ 
                 path('products/',views.get_all_products, name ='products'),
                 path('products/<str:pk>',views.get_specified_product, name ='get_product'),
                 path('products/filter',views.filter_products, name ='filtered_products'),

                 
]             


