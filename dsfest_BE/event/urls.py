from django.urls import path

from . import views

urlpatterns = [
    path('abouts/', views.PostList.as_view()),
]