from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('albums/<int:pk>/', views.AlbumDetail.as_view(), name="album_detail"),
    path('albums/<int:decade>s', views.Decade.as_view(), name="decade"),
    path('albums/<int:decade>s/<int:year>', views.Year.as_view(), name="year"),
    path('accounts/signup', views.Signup.as_view(), name="signup"),

    path('mylist/<slug:this_list>', views.MyListView.as_view(), name="my_list"),
    path('albums/<int:album>/toggle-mylist', views.ToggleMyList.as_view(), name="toggle_my_list"),
]