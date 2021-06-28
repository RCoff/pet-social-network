from django.contrib import admin
from .models import AnimalModel, BehaviorModel, PetProfile, PetPost, Friends

# Register your models here.
admin.site.register(AnimalModel)
admin.site.register(BehaviorModel)
admin.site.register(PetProfile)
admin.site.register(PetPost)
admin.site.register(Friends)
