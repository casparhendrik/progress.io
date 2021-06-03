from django.urls import path
from .views import room_view

app_name = 'rooms'

urlpatterns = [
    path('', room_view, name='home'),
]