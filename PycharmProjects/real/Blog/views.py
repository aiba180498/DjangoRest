from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.shortcuts import render
from Blog.models import Blog
from Blog.serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = [AllowAny]