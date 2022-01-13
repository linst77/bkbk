from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Bkbk

# Create your views here.
class BkbkListView( ListView):
    model = Bkbk

class BkbkCreateView( CreateView):
    model = Bkbk
    template_name_suffix = "_create"
    fields = ['site_name', 'site_url']

class BkbkUpdateView( UpdateView):
    model = Bkbk
    template_name_suffix = "_update"
    fields = ['site_name', 'site_url']

class BkbkDeleteView( DeleteView):
    model = Bkbk
    template_name_suffix = "_delete"
    success_url = reverse_lazy( 'list')

class BkbkDetailView( DetailView):
    model = Bkbk