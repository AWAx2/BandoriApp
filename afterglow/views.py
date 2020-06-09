from django.shortcuts import render, redirect
from django.template import loader
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import PhotoForm, ContactForm
from .models import Photo


class IndexView(generic.TemplateView):
    template_name = 'afterglow/index.html'


class AfterglowDet(generic.FormView):
    template_name = 'afterglow/ag_det.html'
    form_class = PhotoForm
    success_url = reverse_lazy('afterglow:afterglow_det')


class ResultView(generic.View):

    def post(self, request):
        form = PhotoForm(request.POST, request.FILES)
        if not form.is_valid():
            return redirect('afterglow:input_error')

        photo = Photo(image=form.cleaned_data['image'])
        image = photo.detect_main()
        template = loader.get_template('afterglow/result.html')


        context = {
            'photo_name':photo.image.name,
            'photo_data':image,
        }

        return HttpResponse(template.render(context, request))


class InputErrorView(generic.TemplateView):
    template_name = 'afterglow/input_error.html'


class MyProfileView(generic.TemplateView):
    template_name = 'afterglow/my_profile.html'


class ContactView(generic.FormView):
    template_name = 'afterglow/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('afterglow:sent')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        recipients = [settings.EMAIL_HOST_USER]
        send_mail(title, message, email, recipients)
        return redirect('afterglow:contact')



class SentView(generic.TemplateView):
    template_name = 'afterglow/sent.html'
