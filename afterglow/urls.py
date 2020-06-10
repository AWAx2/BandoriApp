from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'afterglow'

urlpatterns = [
    path('sent/', views.SentView.as_view(), name='sent'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('profile/', views.MyProfileView.as_view(), name='my_profile'),
    path('afterglowdet/', views.AfterglowDet.as_view(), name='afterglow_det'),
    path('result/', views.ResultView.as_view(), name='result'),
    path('input-error/', views.InputErrorView.as_view(), name='input_error'),
    path('', views.IndexView.as_view(), name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
