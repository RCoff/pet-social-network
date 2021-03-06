from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('home/', views.Homepage.as_view(), name='home'),
    path('home/add-a-pet/', views.AddAPet.as_view(), name='add_a_pet'),
    path('profile/<uuid:id>', views.PetProfile.as_view(), name='profile'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
