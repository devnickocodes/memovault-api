from django.urls import path
from reports import views

urlpatterns = [
    path('reports/', views.ReportListCreate.as_view()),
]