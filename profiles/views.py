from rest_framework import generics
from .serializers import ProfileSerializer
from .models import Profile
from memovault_api.permissions import IsOwnerOrReadOnly

# Create your views here.


class ProfileList(generics.ListAPIView):

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateAPIView):

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer