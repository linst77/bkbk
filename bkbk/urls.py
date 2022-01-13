from django.urls import path, include
from .views import BkbkListView

urlpatterns = [
    path('', BkbkListView.as_view(), name='list'),
]