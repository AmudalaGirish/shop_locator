from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.shop_list, name='shop_list'),
    path('<int:id>/', views.shop_detail, name='shop_detail'),
    path('create/', views.shop_create, name='shop_create'),
    path('<int:id>/update/', views.shop_update, name='shop_update'),
    path('query/', views.shops_query_view, name='shop_query'),
]