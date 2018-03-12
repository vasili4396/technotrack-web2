from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

import Post.views as post_views

router = routers.DefaultRouter()
router.register(r'', post_views.PostViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]