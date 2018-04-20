from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from User.views import UserViewSet
from Post.views import PostViewSet
from Comment.views import CommentViewSet
from socNetwork import index


routers = DefaultRouter()
routers.register('user', UserViewSet)
routers.register('post', PostViewSet)
routers.register('comment', CommentViewSet, base_name='comment')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('Core.urls', namespace="Core")),
    url(r'^api/', include(routers.urls)),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^$', index.index, name='index_page'),
    url(r'^.*?/$', index.index)
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
