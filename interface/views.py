from django.shortcuts import render
from django.views.generic import View, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404

from data.models import AnimalModel, Friends, PetPost
from .forms import LoginForm


class Index(LoginRequiredMixin, View):
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


class Login(LoginView):
    template_name = 'account/login.html'
    authentication_form = LoginForm
    redirect_field_name = 'index'
