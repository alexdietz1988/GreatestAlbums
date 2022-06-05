from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('albums/<int:pk>/', views.AlbumDetail.as_view(), name="album_detail"),
    path('albums/decade/<int:decade>', views.Decade.as_view(), name="decade"),
    path('accounts/signup', views.Signup.as_view(), name="signup"),

    path('favorites', views.Favorites.as_view(), name="favorites"),
    path('want-to-listen', views.WantToListen.as_view(), name="want_to_listen"),
    path('listened', views.Listened.as_view(), name="listened"),
    path('not-interested', views.NotInterested.as_view(), name="not_interested"),

    path('albums/<int:pk>/add', views.AddToUserList.as_view(), name="add_to_userlist"),
]