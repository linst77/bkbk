from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Bkbk

# Create your views here.
class BkbkListView( ListView):
    model = Bkbk
