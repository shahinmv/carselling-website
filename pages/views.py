from django.shortcuts import render
from .models import Team
from cars.models import Car
from django.http import JsonResponse


# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    title_search = Car.objects.values_list('car_title', flat=True).distinct()
    model_search = Car.objects.values_list('car_model', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()

    
    data = {
        'teams' : teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'title_search': title_search,
        'model_search': model_search,
        'year_search': year_search,
        'city_search': city_search,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams' : teams,
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')

def get_json_car_Data(request):
    qs_val = list(Car.objects.values())
    return JsonResponse({'data':qs_val})

def get_json_model_data(request, *args, **kwargs):
    selected_car = kwargs.get('car_title')
    obj_models = list(Car.objects.values_list('car_model', flat=True).filter(car_title__icontains=selected_car).values())
    return JsonResponse({'data': obj_models})
