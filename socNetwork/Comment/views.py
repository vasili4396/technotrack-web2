from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import list_route


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().prefetch_related('author', 'author__avatar',)
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user).prefetch_related('author', 'author__avatar') \
            if self.action == 'mine' \
            else self.queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @list_route(methods=['get'],
                permission_classes=[permissions.IsAuthenticated])
    def mine(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
