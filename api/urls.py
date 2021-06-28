from django.urls import path
from rest_framework import renderers

from . import views


animal_list = views.AnimalViewset.as_view({
    'get': 'list',
    'put': 'update',
    'post': 'create'
})

behavior_list = views.BehaviorViewset.as_view({
    'get': 'list',
    'put': 'update',
    'post': 'create'
})

urlpatterns = [
    path('animal/', animal_list, name="animal_list"),
    path('behavior/', behavior_list, name="behavior_list")
]
