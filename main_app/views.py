from django import forms
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Album, MyList

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.all()
        return context

class AlbumDetail(TemplateView):
    template_name = "album_detail.html"

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context["album"] = Album.objects.get(pk=pk)
        context["albums"] = Album.objects.all()
        context["favorites"] = MyList.objects.get(user=self.request.user).favorites.all()
        context["want_to_listen"] = MyList.objects.get(user=self.request.user).want_to_listen.all()
        return context

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
            MyList.objects.create(user=user)
            login(request, user)
            return redirect("/")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

class Favorites(TemplateView):
    template_name = "favorites.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["favorites"] = MyList.objects.get(user=self.request.user).favorites.all()
        return context

class WantToListen(TemplateView):
    template_name = "want_to_listen.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["want_to_listen"] = MyList.objects.get(user=self.request.user).want_to_listen.all()
        return context

class Listened(TemplateView):
    template_name = "listened.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["listened"] = MyList.objects.get(user=self.request.user).listened.all()
        return context

class NotInterested(TemplateView):
    template_name = "not_interested.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["not_interested"] = MyList.objects.get(user=self.request.user).not_interested.all()
        return context

class AddToFavorites(View):
    def get(self, request, album):
        MyList.objects.get(user=self.request.user).favorites.add(album)
        return redirect('favorites')

class RemoveFromFavorites(View):
    def get(self, request, album):
        MyList.objects.get(user=self.request.user).favorites.remove(album)
        return redirect('favorites')

class AddWantToListen(View):
    def get(self, request, album):
        MyList.objects.get(user=self.request.user).want_to_listen.add(album)
        return redirect('want_to_listen')

class RemoveWantToListen(View):
    def get(self, request, album):
        MyList.objects.get(user=self.request.user).want_to_listen.remove(album)
        return redirect('want_to_listen')

class AddListened(View):
    def get(self, request, album):
        MyList.objects.get(user=self.request.user).listened.add(album)
        return redirect('listened')

class RemoveListened(View):
    def get(self, request, album):
        MyList.objects.get(user=self.request.user).listened.remove(album)
        return redirect('listened')

class AddNotInterested(View):
    def get(self, request, album):
        MyList.objects.get(user=self.request.user).not_interested.add(album)
        return redirect('not_interested')

class RemoveNotInterested(View):
    def get(self, request, album):
        MyList.objects.get(user=self.request.user).not_interested.remove(album)
        return redirect('not_interested')