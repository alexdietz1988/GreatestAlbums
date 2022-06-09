from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Album, MyList

# Create your views here.
class Landing(TemplateView):
    template_name="landing.html"

class AllAlbums(TemplateView):
    template_name = "all_albums.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.all()
        return context

class AllFilter(TemplateView):
    template_name = "all_filter.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.all()
        if self.request.user.is_authenticated:
            mylist = MyList.objects.get(user=self.request.user)
            context["favorites"] = mylist.favorites.all()
            context["want_to_listen"] = mylist.want_to_listen.all()
            context["listened"] = mylist.listened.all()
            context["not_interested"] = mylist.not_interested.all()
        return context

class AlbumDetail(TemplateView):
    template_name = "album_detail.html"

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context["album"] = Album.objects.get(pk=pk)
        context["albums"] = Album.objects.all()
        if self.request.user.is_authenticated:
            mylist = MyList.objects.get(user=self.request.user)
            context["favorites"] = mylist.favorites.all()
            context["want_to_listen"] = mylist.want_to_listen.all()
            context["listened"] = mylist.listened.all()
            context["not_interested"] = mylist.not_interested.all()
        return context

class Decade(TemplateView):
    template_name = "decade.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.all()
        return context

class DecadeFilter(TemplateView):
    template_name = "decade_filter.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.all()
        if self.request.user.is_authenticated:
            mylist = MyList.objects.get(user=self.request.user)
            context["favorites"] = mylist.favorites.all()
            context["want_to_listen"] = mylist.want_to_listen.all()
            context["listened"] = mylist.listened.all()
            context["not_interested"] = mylist.not_interested.all()
        return context

class Year(TemplateView):
    template_name = "year.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.all()
        return context

class YearFilter(TemplateView):
    template_name = "year_filter.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.all()
        if self.request.user.is_authenticated:
            mylist = MyList.objects.get(user=self.request.user)
            context["favorites"] = mylist.favorites.all()
            context["want_to_listen"] = mylist.want_to_listen.all()
            context["listened"] = mylist.listened.all()
            context["not_interested"] = mylist.not_interested.all()
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

class MyLists(TemplateView):
    template_name = "mylists.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mylist = MyList.objects.get(user=self.request.user)
        context["favorites"] = mylist.favorites.all()
        context["want_to_listen"] = mylist.want_to_listen.all()
        context["listened"] = mylist.listened.all()
        context["not_interested"] = mylist.not_interested.all()
        return context

class SelectedList(TemplateView):
    template_name = "selectedlist.html"

    def get_context_data(self, this_list, **kwargs):
        context = super().get_context_data(**kwargs)
        mylist = MyList.objects.get(user=self.request.user)
        if this_list == "favorites":
            context["albums"] = mylist.favorites.all()
            context["list_title"] = "Favorites"
        if this_list == "want-to-listen":
            context["albums"] = mylist.want_to_listen.all()
            context["list_title"] = "Want to Listen"
        if this_list == "listened":
            context["albums"] = mylist.listened.all()
            context["list_title"] = "Listened"
        if this_list == "not-interested":
            context["albums"] = mylist.not_interested.all()
            context["list_title"] = "Not Interested"
        return context

class ToggleMyList(View):
    def get(self, request, album):
        list = request.GET.get("list")
        toggle = request.GET.get("toggle")
        mylist = MyList.objects.get(user=self.request.user)

        if list == "favorites": list = mylist.favorites
        if list == "want_to_listen": list = mylist.want_to_listen
        if list == "listened": list = mylist.listened
        if list == "not_interested": list = mylist.not_interested

        if toggle == "add": list.add(album)
        if toggle == "remove": list.remove(album)
        return redirect('album_detail', pk=album)