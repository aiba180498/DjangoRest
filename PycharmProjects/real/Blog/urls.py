from rest_framework.routers import DefaultRouter

from Blog.views import BlogViewSet

router = DefaultRouter()

router.register(r'Blog', BlogViewSet, base_name='Blog')