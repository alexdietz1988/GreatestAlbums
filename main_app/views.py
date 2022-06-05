from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Album, UserList

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.all()
        context['userlists'] = UserList.objects.all()
        return context

class AlbumDetail(DetailView):
    model = Album
    template_name = "album_detail.html"

class Decade(TemplateView):
    template_name = "decade.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.all()
        return context

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

class Favorites(TemplateView):
    template_name = "userlist/favorites.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.all()
        context['userlists'] = UserList.objects.all()
        return context

class WantToListen(TemplateView):
    template_name = "userlist/wanttolisten.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.all()
        context['userlists'] = UserList.objects.all()
        return context

class Listened(TemplateView):
    template_name = "userlist/listened.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.all()
        context['userlists'] = UserList.objects.all()
        return context

class NotInterested(TemplateView):
    template_name = "userlist/notinterested.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.all()
        context['userlists'] = UserList.objects.all()
        return context