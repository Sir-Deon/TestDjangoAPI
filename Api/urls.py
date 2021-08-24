from django.urls import path
from . import views


urlpatterns = [
    path('', views.test, name='test'),
    path('list_cities/', views.listCity, name='list_cities'),
    path('add_city/', views.addCity, name='add_city'),
    path('update_city/<str:pk>/', views.updateCity, name='update_city'),
    path('delete_city/<str:pk>/', views.deleteCity, name='delete_city'),
]
