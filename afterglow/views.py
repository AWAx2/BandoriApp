from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages


class TopPageView(generic.TemplateView):
    template_name = 'afterglow/top.html'
