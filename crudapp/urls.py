from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_task/<str:pk>', views.update, name = 'update'),
    path('delete_items/<str:pk>', views.delete, name = 'delete'),
]