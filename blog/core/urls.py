from django.conf.urls import url
from core.views import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name ='mainpg'),
    url(r'^login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^register/', RegistrationView.as_view(template_name='core/user_form.html'), name='register')
]