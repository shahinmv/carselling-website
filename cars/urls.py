from django.urls import path
from . import views


urlpatterns = [
    path('', views.cars, name = 'cars'),
    path('<int:id>', views.car_detail, name = 'car_detail'),
    path('search', views.search, name = 'search'),

    path('cars-json/', views.get_json_car_Data, name = 'cars-json'),
    path('models-json/<str:car_title>/', views.get_json_model_data, name = 'models-json'),
]