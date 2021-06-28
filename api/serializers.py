from rest_framework import serializers

from data.models import AnimalModel, BehaviorModel


class AnimalModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalModel
        fields = '__all__'


class BehaviorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BehaviorModel
        fields = '__all__'
