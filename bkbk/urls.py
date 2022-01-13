from django.urls import path, include
from .views import *

urlpatterns = [
    path('', BkbkListView.as_view(), name='list'),
    path('create/', BkbkCreateView.as_view(), name='create'),
    path('update/<int:pk>', BkbkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BkbkDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>', BkbkDetailView.as_view(), name='detail'),

]