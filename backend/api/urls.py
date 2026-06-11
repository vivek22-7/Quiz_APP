from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('dashboard/', views.dashboard),
    path('items/', views.item_list),          # list + create
    path('items/<int:pk>/', views.item_detail),  # get + update + delete
]


