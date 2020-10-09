from django.urls import path
from .views import Orderpageview

urlpatterns=[
    path('',Orderpageview.as_view(),name='orders'),
]