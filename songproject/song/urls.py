from  django.urls import path
from .views import add_song, show_song, update_song, delete_song

urlpatterns = [
    path('add/', add_song, name='add_url'),
    path('show/', show_song, name='show_url'),
    path('update/<int:pk>/', update_song, name='update_url'),
    path('delete/<int:pk>/', delete_song, name='delete_url'),
]
