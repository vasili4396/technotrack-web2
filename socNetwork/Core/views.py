from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('users:user-list', request=request, format=format),
        'posts': reverse('posts:post-list', request=request, format=format),
    })


def home(request):
    return render(request, 'home.html')
