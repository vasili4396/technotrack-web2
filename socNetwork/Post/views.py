from rest_framework import permissions, viewsets, status
from rest_framework.decorators import list_route
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().prefetch_related('author', 'author__avatar', 'comments')
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).prefetch_related('author', 'author__avatar') \
            if self.action == 'mine' \
            else self.queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @list_route(methods=['get'],
                permission_classes=[permissions.IsAuthenticated])
    def mine(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

