from django import forms
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Album, UserList, User

# Create your views here.
class AddForm(forms.Form):
    want_to_listen = forms.BooleanField()

class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.all()
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
        context['userlists'] = UserList.objects.filter(user=self.request.user)
        return context

class WantToListen(TemplateView):
    template_name = "userlist/wanttolisten.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userlists'] = UserList.objects.filter(user=self.request.user)
        return context

class Listened(TemplateView):
    template_name = "userlist/listened.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userlists'] = UserList.objects.filter(user=self.request.user)
        return context

class NotInterested(TemplateView):
    template_name = "userlist/notinterested.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userlists'] = UserList.objects.filter(user=self.request.user)
        return context

class AddToUserList(View):
    def post(self, request, pk):
        user = self.request.user
        album = Album.objects.get(pk=pk)

        if request.POST.get("want_to_listen"): want_to_listen = request.POST.get("want_to_listen")
        else: want_to_listen = False
        if request.POST.get("listened"): listened = request.POST.get("listened")
        else: listened = False
        if request.POST.get("favorite"): favorite = request.POST.get("favorite")
        else: favorite = False
        if request.POST.get("not_interested"): not_interested = request.POST.get("not_interested")
        else: not_interested = False

        UserList.objects.create(user=user, album=album, want_to_listen=want_to_listen, listened=listened, favorite=favorite, not_interested=not_interested)
        return redirect('album_detail', pk=pk)