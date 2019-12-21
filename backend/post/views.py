from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from . import models
from . import serializers

class PostViewset(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

class ImageViewset(viewsets.ModelViewSet):
	queryset = Image.objects.all().order_by('id')
	serializer_class = ImageSerializer
