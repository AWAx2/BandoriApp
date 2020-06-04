from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'afterglow'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('afterglowdet/', views.AfterglowDet.as_view(), name='afterglow_det'),
    path('result/', views.ResultView.as_view(), name='result'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
