from django.urls import path

from . import views

app_name = 'postpartumdepression'

urlpatterns = [
    path('home/', views.home, name='home'),
]