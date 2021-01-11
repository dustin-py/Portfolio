from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('thmprofile/', views.thm_profile, name='thm_profile'),
    path('thmprofile/thmbadges/', views.thm_badges, name='thm_badges'),
]