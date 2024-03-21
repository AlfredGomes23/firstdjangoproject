from . import views
from django.urls import path


urlpatterns = [
    path('dlogin', views.dlogin, name="dlogin")
]

