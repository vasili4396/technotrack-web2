from django.conf.urls import url
from .views import CommentViewSet

urlpatterns = [
    url(r'^', CommentViewSet, name='comment'),
]