# pages/urls.py
from django.urls import path
from .views import PromiseCreateView

urlpatterns = [
    path('', PromiseCreateView.as_view(), name='create')
]
