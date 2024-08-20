from rest_framework import generics, permissions, filters
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from memovault_api.permissions import IsAdmin, IsOwnerOrReadOnly
from .models import Report
from posts.models import Post
from .serializers import ReportSerializer



class ReportListCreate(generics.ListCreateAPIView):
    """
    List all reports or create a new report.

    This view provides two functionalities:
    - List all reports submitted by the authenticated user, with the ability to
                                         filter, order, and search the results.
    - Allows authenticated users to create a new report, associating it with
                                               the current user as the owner.

    Attributes:
        serializer_class (Serializer): Specifies the serializer to use for
                                                                      the view.
        permission_classes (list): Specifies the permissions required to
                                                            access the view.
        filter_backends (list): Specifies the filter backends used for
                                    filtering, searching, and ordering reports.
        filterset_fields (list): The fields used for filtering reports.
        ordering_fields (list): The fields that can be used for
                                               ordering reports.

    Methods:
        get_queryset: Retrieves the list of reports for the authenticated
                                    user or raises a `NotAuthenticated`
                                    exception if the user is not logged in.
        perform_create: Associates the created report with the authenticated
                                                           user as the owner.
    """
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
        return Report.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        post_id = self.request.data.get('post')
        if self.request.user == Post.objects.get(id=post_id).owner:
            raise PermissionDenied("You cannot report your own post.")
        serializer.save(owner=self.request.user)


class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific report.

    This view allows authenticated users to:
    - Retrieve a report submitted by themselves.
    - Update a report if they are the owner.
    - Delete a report if they are the owner.

    Attributes:
        serializer_class (Serializer): Specifies the serializer to use
                                                          for the view.
        permission_classes (list): Specifies the permissions required
                                                   to access the view.

    Methods:
        get_queryset: Retrieves the report for the authenticated user or
                      raises a `NotAuthenticated` exception if the user
                      is not logged in.
    """
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Report.objects.filter(owner=self.request.user)


class AdminReportList(generics.ListAPIView):
    """
    List all reports for administrators.

    This view provides a list of all reports, accessible only to users with
    admin privileges. Reports can be filtered and ordered.

    Attributes:
        serializer_class (Serializer): Specifies the serializer to use for
                                                                  the view.
        permission_classes (list): Specifies the permissions required to access
                                                   the view (admin users only).
        queryset (QuerySet): The queryset used to retrieve all reports.
        filter_backends (list): Specifies the filter backends used for
                                        filtering and ordering reports.
        filterset_fields (list): The fields used for filtering reports.
        ordering_fields (list): The fields that can be used for
                                               ordering reports.
    """
    serializer_class = ReportSerializer
    permission_classes = [IsAdmin]
    queryset = Report.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        'owner',
        'post',
        'reason',
    ]
    ordering_fields = [
        'created_at',
        '-created_at'
    ]


class AdminReportDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or delete a specific report for administrators.

    This view allows administrators to retrieve or delete any report.

    Attributes:
        serializer_class (Serializer): Specifies the serializer to use
                                                          for the view.
        permission_classes (list): Specifies the permissions required
                                                   to access the view.
        queryset (QuerySet): The queryset used to retrieve all reports.
    """
    serializer_class = ReportSerializer
    permission_classes = [IsAdmin]
    queryset = Report.objects.all()
