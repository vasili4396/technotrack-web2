from django.conf.urls import url, include
import Post.views as post_views


urlpatterns = [
    url(r'^$', post_views.PostViewSet, name='post-list'),
]