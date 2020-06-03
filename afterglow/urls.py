from django.urls import path
from . import views


app_name = 'afterglow'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('afterglowdet/', views.AfterglowDet.as_view(), name='afterglow_det'),
    path('result/', views.ResultView.as_view(), name='result'),
]
