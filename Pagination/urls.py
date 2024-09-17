from django.urls import path
from .views import page

app_name = 'pagination'

urlpatterns = [
    path('page/', page)
]