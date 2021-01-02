from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_clubs, name='clubs'),
    path('<int:club_id>/', views.club_detail, name='club_detail'),
    path('add/', views.add_club, name='add_club'),
]