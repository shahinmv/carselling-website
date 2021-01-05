from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('cars-json/', views.get_json_car_Data, name = 'cars-json'),
    path('models-json/<str:car_title>/', views.get_json_model_data, name = 'models-json'),
    path('about', views.about, name = 'about'),
    path('services', views.services, name = 'services'),
    path('contact', views.contact, name = 'contact'),
]