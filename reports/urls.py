from django.urls import path
from reports import views

urlpatterns = [
    path('reports/', views.ReportListCreate.as_view()),
    path('reports/<int:pk>/', views.ReportDetailView.as_view()),
]