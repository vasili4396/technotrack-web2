from rest_framework import generics
from User.models import CustomUser

from django.http import HttpResponseRedirect
from rest_framework import reverse


# class RegistrationPage(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = RegistrationSerializer
#     permission_classes = ()
#
#     def create(self, request, *args, **kwargs):
#         # response = super(RegistrationPage, self).get_object().username
#         # here may be placed additional operations for
#         # extracting id of the object and using reverse()
#         # redirect('User:user-page', username='vasili13')
#         return redirect('Post:post-list') #kwargs={'username': 'vasili13'})

#
# def home(request):
#     return render(request, 'home.html')
