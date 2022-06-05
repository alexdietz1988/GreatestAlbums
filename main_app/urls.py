from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('albums/<int:pk>/', views.AlbumDetail.as_view(), name="album_detail"),
    path('albums/decade/<int:decade>', views.Decade.as_view(), name="decade"),
    path('accounts/signup', views.Signup.as_view(), name="signup"),

    path('favorites', views.FavoritesPage.as_view(), name="favorites"),
    path('want-to-listen', views.WantToListenPage.as_view(), name="want_to_listen"),
    path('listened', views.ListenedPage.as_view(), name="listened"),
    path('not-interested', views.NotInterestedPage.as_view(), name="not_interested"),
]