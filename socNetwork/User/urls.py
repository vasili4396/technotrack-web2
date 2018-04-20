from django.conf.urls import url, include
import User.views as user_views

urlpatterns = [
    url(r'', user_views.UserViewSet, name='user-list'),
]