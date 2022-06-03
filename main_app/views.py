from django.views.generic.base import TemplateView
from .models import Album
from django.views.generic import DetailView

# Create your views here.
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