from rest_framework import viewsets, permissions
from .models import CustomUser
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.IsAuthenticated, )

# class UserList(generics.ListCreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = UserSerializer
#
#     def get_queryset(self):
#         return CustomUser.objects.all().filter(username=self.request.email)


