from django.urls import path
from . import views

urlpatterns = [
    path('', views.Landing.as_view(), name="landing"),
    path('accounts/signup', views.Signup.as_view(), name="signup"),

    path('all/<int:page>', views.AllAlbums.as_view(), name="all_albums"),
    path('<int:decade>s', views.Decade.as_view(), name="decade"),
    path('<int:decade>s/<int:year>', views.Year.as_view(), name="year"),

    path('albums/<int:pk>/', views.AlbumDetail.as_view(), name="album_detail"),

    path('all/filter/', views.AllFilter.as_view(), name="all_filter"),
    path('<int:decade>s/filter', views.DecadeFilter.as_view(), name="decade_filter"),
    path('<int:decade>s/<int:year>/filter', views.YearFilter.as_view(), name="year_filter"),

    path('mylists', views.MyLists.as_view(), name="my_lists"),
    path('mylists/<slug:this_list>', views.SelectedList.as_view(), name="selected_list"),
    path('albums/<int:album>/toggle-mylist', views.ToggleMyList.as_view(), name="toggle_my_list"),
]