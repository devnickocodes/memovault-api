from rest_framework import generics, permissions
from rest_framework.exceptions import NotAuthenticated
from .models import Report
from .serializers import ReportSerializer

class ReportListCreate(generics.ListCreateAPIView):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Report.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Report.objects.filter(owner=self.request.user)
        else:
            raise NotAuthenticated("You must be logged in to access this report.")


