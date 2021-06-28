import uuid

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class AnimalModel(models.Model):
    animal_choices = (
        ('dog', 'dog'),
        ('cat', 'cat')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    animal_type = models.CharField(max_length=140, choices=animal_choices)
    animal_name = models.CharField(max_length=140)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    age_years = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        unique_together = ['owner', 'animal_type', 'animal_name']


class BehaviorModel(models.Model):
    animal_choices = (
        ('Good', 'Good'),
        ('Bad', 'Bad')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    animal = models.ForeignKey(AnimalModel, on_delete=models.CASCADE)
    behavior = models.CharField(choices=animal_choices, max_length=140)
    modified = models.DateField(auto_now=True)


def get_upload_path(instance, filename):
    return f"user_{instance.id.owner}/{filename}"


class PetProfile(models.Model):
    id = models.OneToOneField(AnimalModel, primary_key=True, on_delete=models.CASCADE)
    profile_description = models.CharField(max_length=512, blank=True, null=True)
    profile_image = models.ImageField(upload_to=get_upload_path, blank=True, null=True, max_length=150)


class PetPost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.ForeignKey(PetProfile, on_delete=models.CASCADE)
    content = models.CharField(max_length=512, blank=False)
    attachment = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    created = models.DateTimeField(auto_now=True, editable=False)


class Friends(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    animal = models.ForeignKey(AnimalModel, on_delete=models.CASCADE, related_name='animal_friend_set')
    friend = models.ForeignKey(AnimalModel, on_delete=models.CASCADE, related_name='friend_friend_set')
    created = models.DateTimeField(auto_now=True, editable=False)


class PetLinkedAccount(models.Model):
    ACCOUNT_TYPE_CHOICES = (
        ('Instagram', 'Instagram'),
        ('Twitter', 'Twitter'),
        ('Facebook', 'Facebook'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account_type = models.CharField(max_length=25, choices=ACCOUNT_TYPE_CHOICES, editable=False, blank=False)
    account_url = models.URLField(editable=False, blank=False)
    created = models.DateTimeField(auto_now=True, editable=False)
