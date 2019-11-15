from django.shortcuts import render
from rest_framework import viewsets

from festas.models import Festa
from festas.serializers import FestaSerializer


class FestaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Festa.objects.all().order_by('-data_inicio')
    serializer_class = FestaSerializer
