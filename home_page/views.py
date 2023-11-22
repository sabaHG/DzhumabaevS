from django.shortcuts import render, get_object_or_404
from .models import CarModel, Afisha, Slider


def car_post_view(request):
    if request.method == 'GET':
        car_list = CarModel.objects.all()

        return render(request, template_name='main/index.html',
                      context={
                          'car_list': car_list,


                      })

def car_detail_view(request, id):
    if request.method == 'GET':
        car_id = get_object_or_404(CarModel, id=id)
        return render(request, template_name='main/car_detail.html', context={'car_id': car_id})


def detail_view(request):
    afisha = Afisha.objects.all()
    slider = Slider.objects.all()
    return render(request, template_name='main/detail.html', context={
        'afisha': afisha,
        'slider_list': slider})