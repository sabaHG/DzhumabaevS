from django.urls import path
from .views import car_post_view , car_detail_view , detail_view

urlpatterns = [
    path('home_page/', car_post_view),
    path('car_detail/<int:id>/', car_detail_view),
    path('detail/' , detail_view , name = 'detail')
]