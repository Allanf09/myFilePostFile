from django.urls import path

from . import views

app_name = 'share_files'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('upload', views.upload, name='upload'),
    path('search_file/', views.search_file, name='search_file'),
]