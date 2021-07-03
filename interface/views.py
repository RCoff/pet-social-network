from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View, ListView, TemplateView, FormView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from django.urls import reverse

from data.models import AnimalModel, Friends, PetPost
from .forms import LoginForm, AddAPetForm, PetProfileForm


class Index(View):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)


class Homepage(LoginRequiredMixin, ListView):
    template_name = 'account/homepage.html'
    context_object_name = 'owned_animals_list'

    def get_queryset(self):
        return AnimalModel.objects.filter(owner=self.request.user)


class PetProfile(LoginRequiredMixin, View):
    template_name = 'account/profile.html'
    profile_id = None
    profile = None

    def __init__(self):
        super().__init__()
        self.friend_posts_list = None

    def get(self, request, *args, **kwargs):
        self.profile_id = self.kwargs.get('id', None)
        self.profile = get_object_or_404(AnimalModel, id=self.profile_id)
        self.friend_posts_list = self.friend_posts()
        # profile = profile.objects.select_related()

        return render(request, self.template_name, {'profile': self.profile,
                                                    'friend_posts': self.friend_posts_list})

    def friend_posts(self):
        qs = Friends.objects.select_related('friend').filter(animal=self.profile_id)
        return qs


class AddAPet(LoginRequiredMixin, View):
    template_name = 'account/add_a_pet.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': AddAPetForm,
                                                    'profile_form': PetProfileForm})

    def post(self, request, *args, **kwargs):
        form = AddAPetForm(request.POST)
        profile_form = PetProfileForm(request.POST)

        if form.is_valid():
            animal_form = form.save(commit=False)
            animal_form.owner = request.user

            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.id = animal_form
                animal_form.save()
                profile.save()
            else:
                animal_form.save()

            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, self.template_name, {'form': AddAPetForm,
                                                        'profile_form': PetProfileForm,
                                                        'form_not_valid': True})


class Login(LoginView):
    template_name = 'account/login.html'
    authentication_form = LoginForm


class Logout(LoginRequiredMixin, View):
    redirect_url_name = 'index'

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse(self.redirect_url_name))
