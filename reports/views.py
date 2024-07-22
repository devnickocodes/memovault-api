from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import NotAuthenticated
from .models import Report
from .serializers import ReportSerializer
from memovault_api.permissions import IsAdmin, IsOwnerOrReadOnly


class ReportListCreate(generics.ListCreateAPIView):

    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = [
        'post',
    ]
    ordering_fields = [
        'created_at',
        '-created_at'
    ]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Report.objects.filter(owner=self.request.user)
        else:
            raise NotAuthenticated("You must be logged in to view reports.")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Report.objects.filter(owner=self.request.user)
        else:
            raise NotAuthenticated("You must be logged in to access this report.")


class AdminReportList(generics.ListAPIView):
    serializer_class = ReportSerializer
    permission_classes = [IsAdmin]
    queryset = Report.objects.all()

class AdminReportDetail(generics.RetrieveDestroyAPIView):
    serializer_class = ReportSerializer
    permission_classes = [IsAdmin]
    queryset = Report.objects.all()