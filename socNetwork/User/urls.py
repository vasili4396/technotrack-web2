from django.conf.urls import url, include
from User import views
from django.contrib import admin
from rest_framework import routers
import User.views as user_views

router = routers.DefaultRouter()
router.register(r'', user_views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
#
# urlpatterns = [
#     url(r'^', views.UserList.as_view(), name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
# ]


# Format suffixes
# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
