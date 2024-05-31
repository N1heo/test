from rest_framework import viewsets
from .models import Conference, Role, ConfUser
from .serializers import ConferenceSerializer, RoleSerializer, ConfUserSerializer
from .permissions import IsSuperUser, IsSuperUserOrPostOnly, AllowPostForAll
from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUser]


class ConferenceViewSet(viewsets.ModelViewSet):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer
    permission_classes = [IsSuperUser]


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsSuperUser]


class ConfUserViewSet(viewsets.ModelViewSet):
    queryset = ConfUser.objects.all()
    serializer_class = ConfUserSerializer

