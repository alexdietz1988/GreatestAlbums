from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('albums/<int:pk>/', views.AlbumDetail.as_view(), name="album_detail"),
    path('albums/<int:decade>s', views.Decade.as_view(), name="decade"),
    path('albums/<int:decade>s/<int:year>', views.Year.as_view(), name="year"),
    path('accounts/signup', views.Signup.as_view(), name="signup"),

    path('favorites', views.Favorites.as_view(), name="favorites"),
    path('albums/<int:album>/add-favorites', views.AddToFavorites.as_view(), name="add_to_favorites"),
    path('albums/<int:album>/remove-favorites', views.RemoveFromFavorites.as_view(), name="remove_from_favorites"),

    path('want-to-listen', views.WantToListen.as_view(), name="want_to_listen"),
    path('albums/<int:album>/add-want-to-listen', views.AddWantToListen.as_view(), name="add_want_to_listen"),
    path('albums/<int:album>/remove-want-to-listen', views.RemoveWantToListen.as_view(), name="remove_want_to_listen"),

    path('listened', views.Listened.as_view(), name="listened"),
    path('albums/<int:album>/add-listened', views.AddListened.as_view(), name="add_listened"),
    path('albums/<int:album>/remove-listened', views.RemoveListened.as_view(), name="remove_listened"),

    path('not_interested', views.NotInterested.as_view(), name="not_interested"),
    path('albums/<int:album>/not-interested', views.AddNotInterested.as_view(), name="add_not_interested"),
    path('albums/<int:album>/remove-not-interested', views.RemoveNotInterested.as_view(), name="remove_not_interested"),
]