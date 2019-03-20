from django.contrib.auth.models import User, Group
from rest_framework import authentication, permissions, viewsets, filters
from .serializers import UserSerializer, GroupSerializer

class DefaultsMixin(object):
    """Default settings for view authentication, permissions, filtering
     and pagination."""

    # TODO If you wish, you can change API permissions here
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    # filter_backends = (
    #     filters.DjangoFilterBackend,
    #     filters.SearchFilter,
    #     filters.OrderingFilter,
    # )

class UserViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

