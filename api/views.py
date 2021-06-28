from rest_framework import viewsets

from data.models import AnimalModel, BehaviorModel
from . import serializers


class AnimalViewset(viewsets.ModelViewSet):
    queryset = AnimalModel.objects.all()
    serializer_class = serializers.AnimalModelSerializer

    def perform_create(self, serializer):
        serializer.save()


class BehaviorViewset(viewsets.ModelViewSet):
    queryset = BehaviorModel.objects.all()
    serializer_class = serializers.BehaviorModelSerializer

    def perform_create(self, serializer):
        serializer.save()
