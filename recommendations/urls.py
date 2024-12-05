from django.urls import path

from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('recommendations/', views.recommend_movies_view, name="recommendations"),
    path('contact/', views.contact_feedback, name='contact_feedback'),
]