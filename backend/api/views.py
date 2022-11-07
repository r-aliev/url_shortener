from django.shortcuts import redirect

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import URLMapper
from .serializers import URLMapperSerializer
from .utils import get_shorten_url
from .exceptions import URLIsNotValid


@api_view(['GET'])
def get_urls(request):
    """API endpoint to get all shortened urls"""
    queryset = URLMapper.objects.all()
    serializer = URLMapperSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_url(request):
    """API endpoint to shorten a url"""
    serializer = URLMapperSerializer(data=request.data)

    if serializer.is_valid():
        original_url = serializer.data.get("original_url")
        try:
            shortened_url = get_shorten_url(request, original_url)
        except URLIsNotValid as err:
            content = {'message': str(err)}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        URLMapper.objects.create(original_url=original_url, shortened_url=shortened_url)
        return Response("URL shortened successfully!")


@api_view(['GET'])
def redirect_to_url(request, slug):
    """An endpoint to redirect shortened urls to original urls."""
    shortened_url = request.build_absolute_uri("/" + slug)
    url = URLMapper.objects.get(shortened_url=shortened_url)
    response = redirect(url.original_url)
    return response
