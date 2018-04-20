from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from .models import CustomUser
from .serializers import UserSerializer, SimpleUserSerializer, UserChangePasswordSerializer, RegistrationSerializer
from .permissions import UserPermission


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().prefetch_related('avatar')
    serializer_class = UserSerializer
    permission_classes = (UserPermission, )
    lookup_field = 'username'

    def get_serializer_class(self):
        if self.action == 'list':
            return SimpleUserSerializer
        if self.action == 'retrieve':
            return UserSerializer
        if self.action == 'create':
            return RegistrationSerializer
        if self.action == 'change_password':
            return UserChangePasswordSerializer
        else:
            return UserSerializer

    @detail_route(methods=['get', 'put', 'patch'])
    def change_password(self, request, username=None):
        serializer = UserChangePasswordSerializer(data=request.data)
        # TODO: ПАЧИМУ
        self.get_object()
        #
        if serializer.is_valid():
            serializer.update(self.request.user, serializer.validated_data)
            return Response({'status': 'password changed'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

# class UserPage(generics.RetrieveUpdateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly, )
#     lookup_field = 'username'
#
#
# class UserList(generics.ListAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = SimpleUserSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     http_method_names = ['get']
#
#
# class UserChangePassword(generics.UpdateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserChangePasswordSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
#     lookup_field = 'username'
#
#
# class UserRegister(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = RegistrationSerializer
#     permission_classes = (permissions.AllowAny, )
#
#     def create(self, request, *args, **kwargs):
#         return redirect('Post:post-list')
