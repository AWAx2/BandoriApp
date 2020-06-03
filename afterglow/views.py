from django.shortcuts import render, redirect
from django.template import loader
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from .forms import PhotoForm
from .models import Photo


class IndexView(generic.TemplateView):
    template_name = 'afterglow/index.html'


class AfterglowDet(generic.FormView):
    template_name = 'afterglow/ag_det.html'
    form_class = PhotoForm
    success_url = reverse_lazy('afterglow:afterglow_det')


class ResultView(generic.View):

    def post(self, request, *args, **kwargs):
        form = PhotoForm(request.POST, request.FILES)
        if not form.is_valid():
            raise ValueError('Formが不正です')

        photo = Photo(image=form.cleaned_data['image'])
        image = Photo.detect_main()

        template = loader.get_template('afterglow/result.html')

        context = {
            'image_name':photo.image.name,
        }

        return HttpResponse(template)
