from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .serializers import BookSerializer
from ..models import *


class BookAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
