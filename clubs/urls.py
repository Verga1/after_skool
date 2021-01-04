from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_clubs, name='clubs'),
    path('<int:club_id>/', views.club_detail, name='club_detail'),
    path('add/', views.add_club, name='add_club'),
    path('edit/<int:club_id>/', views.edit_club, name='edit_club'),
    path('delete/<int:club_id>/', views.delete_club, name='delete_club'),
]
