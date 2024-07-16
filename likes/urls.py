from django.urls import path
from likes import views

urlpatterns = [
    path('like/post/', views.PostLikeList.as_view()),
    path('like/post/<int:pk>/', views.PostLikeDetail.as_view()),
]
