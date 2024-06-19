from django.urls import path
from . import views

urlpatterns = [ 
                 path('products/',views.get_all_products, name ='products'),
                 path('products/<str:pk>',views.get_specified_product, name ='get_product'),
                 path('products/filter',views.filter_products, name ='filtered_products'),
                 path('products/add/',views.new_products, name ='new_products'),                 
                path('products/update/<str:pk>',views.edit_products, name ='edit_product'),
                path('<str:pk>/review/',views.add_review, name ='add_review'),
                path('products/delete/<str:pk>',views.delete_products, name ='delete_product'),



                 


                 
]             


