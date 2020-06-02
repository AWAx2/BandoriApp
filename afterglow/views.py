from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages


class IndexView(generic.TemplateView):
    template_name = 'index.html'
