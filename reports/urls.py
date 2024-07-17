from django.urls import path
from reports import views

urlpatterns = [
    path('reports/', views.ReportListCreate.as_view()),
    path('reports/<int:pk>/', views.ReportDetail.as_view()),
    path('reports/admin/', views.AdminReportList.as_view()),
    path('reports/admin/<int:pk>/', views.AdminReportDetail.as_view()),
]