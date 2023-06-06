from django.urls import path
from . import views

urlpatterns = [
    path('shops/', views.shop_list, name='shop_list'),
    path('shops/<int:id>/', views.shop_detail, name='shop_detail'),
    path('shops/create/', views.shop_create, name='shop_create'),
    path('shops/<int:id>/update/', views.shop_update, name='shop_update'),
    path('shops/query/', views.shops_query_view, name='shop_query'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.home, name='home'),
]
