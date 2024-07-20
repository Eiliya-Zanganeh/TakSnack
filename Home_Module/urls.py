from django.urls import path

from Home_Module.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home_url')
]