from django.urls import path
from tasks.views import *

urlpatterns = [
    path('',register_page,name='register_page'),
    path('register/',register_page,name='register_page'),
    path('login/',login_page,name='login_page'),
    path('home_page/',home_page,name='home_page'),
    path('logout/',logout_page,name='logout_page'),

    path('profile/',user_profile,name="user_profile"),
    path('update-profile',update_profile,name='update_profile'),
    path('product-list/',product_list,name='product_list'),
    path('add-product/',add_product,name='add_product'),
]