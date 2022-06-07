from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('albums/<int:pk>/', views.AlbumDetail.as_view(), name="album_detail"),
    path('albums/<int:decade>s', views.Decade.as_view(), name="decade"),
    path('albums/<int:decade>s/<int:year>', views.Year.as_view(), name="year"),
    path('accounts/signup', views.Signup.as_view(), name="signup"),

    path('favorites', views.Favorites.as_view(), name="favorites"),
    path('want-to-listen', views.WantToListen.as_view(), name="want_to_listen"),
    path('listened', views.Listened.as_view(), name="listened"),
    path('not_interested', views.NotInterested.as_view(), name="not_interested"),

    path('albums/<int:album>/toggle-favorite', views.ToggleFavorite.as_view(), name="toggle_favorite"),
    path('albums/<int:album>/toggle-want-to-listen', views.ToggleWantToListen.as_view(), name="toggle_want_to_listen"),
    path('albums/<int:album>/toggle-listened', views.ToggleListened.as_view(), name="toggle_listened"),
    path('albums/<int:album>/toggle-not_interested', views.ToggleNotInterested.as_view(), name="toggle_not_interested"),
]