from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from Core.views import api_root

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('Core.urls', namespace="Core")),


    # url(r'^docs/', include_docs_urls(title='social network API')),
    url(r'^users/', include('User.urls', namespace='User')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^post/', include('Post.urls', namespace='Post')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
