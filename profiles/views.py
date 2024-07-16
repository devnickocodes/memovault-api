from rest_framework import generics
from .serializers import ProfileSerializer
from .models import Profile

# Create your views here.


class ProfileList(generics.ListAPIView):


    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateAPIView):


    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer