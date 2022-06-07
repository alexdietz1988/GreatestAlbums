from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllAlbums.as_view(), name="home"),
    path('albums', views.AllAlbums.as_view(), name="all_albums"),
    path('accounts/signup', views.Signup.as_view(), name="signup"),
    path('albums/<int:decade>s', views.Decade.as_view(), name="decade"),
    path('albums/<int:decade>s/<int:year>', views.Year.as_view(), name="year"),

    path('albums/<int:pk>/', views.AlbumDetail.as_view(), name="album_detail"),

    path('mylist/<slug:this_list>', views.MyListView.as_view(), name="my_list"),
    path('albums/<int:album>/toggle-mylist', views.ToggleMyList.as_view(), name="toggle_my_list"),
]