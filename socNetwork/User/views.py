from rest_framework import viewsets, permissions
from .models import CustomUser
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return CustomUser.objects.all()
