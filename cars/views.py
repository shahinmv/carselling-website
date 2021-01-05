from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse

# Create your views here.

def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    title_search = Car.objects.values_list('car_title', flat=True).distinct()
    model_search = Car.objects.values_list('car_model', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()

    data = {
        'cars': paged_cars,
        'title_search': title_search,
        'model_search': model_search,
        'year_search': year_search,
        'city_search': city_search,
    }
    return render(request, 'cars/cars.html', data)

def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)
    data = {
        'single_car': single_car,
    }
    return render(request, 'cars/car_detail.html', data)

def get_json_car_Data(request):
    qs_val = list(Car.objects.values())
    return JsonResponse({'data':qs_val})

def get_json_model_data(request, *args, **kwargs):
    selected_car = kwargs.get('car_title')
    obj_models = list(Car.objects.values_list('car_model', flat=True).filter(car_title__icontains=selected_car).values())
    return JsonResponse({'data': obj_models})

def search(request):
    cars = Car.objects.order_by('-created_date')

    title_search = Car.objects.values_list('car_title', flat=True).distinct()
    model_search = Car.objects.values_list('car_model', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            cars = cars.filter(car_title__iexact=title)
            
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(car_model__iexact=model)

    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            cars = cars.filter(city__iexact=location)

    if 'year-min' in request.GET:
        yearmin = request.GET['year-min']
        if yearmin:
            cars = cars.filter(year__gte=yearmin)

    if 'year-max' in request.GET:
        yearmax = request.GET['year-max']
        if yearmax:
            cars = cars.filter(year__lte=yearmax)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
           cars = cars.filter(price__gte=min_price, price__lte=max_price)


    data = {
        'cars': cars,
        'title_search': title_search,
        'model_search': model_search,
        'year_search': year_search,
        'city_search': city_search,
    }
    return render(request, 'cars/search.html', data)