# Generated by Django 3.2.4 on 2021-06-25 22:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('animal_type', models.CharField(choices=[('dog', 'dog'), ('cat', 'cat')], max_length=140)),
                ('animal_name', models.CharField(max_length=140, unique=True)),
                ('age_years', models.PositiveSmallIntegerField()),
            ],
            options={
                'unique_together': {('animal_type', 'animal_name')},
            },
        ),
        migrations.CreateModel(
            name='BehaviorModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('behavior', models.CharField(choices=[('Good', 'Good'), ('Bad', 'Bad')], max_length=140)),
                ('date', models.DateField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.animalmodel')),
            ],
        ),
    ]
