from django.urls import path
from likes import views

urlpatterns = [
    path('like/post/', views.PostLike.as_view()),
]
