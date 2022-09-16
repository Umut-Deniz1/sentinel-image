from django.urls import include, path
from rest_framework import routers
from case.api.views import SentinelImageView

router = routers.DefaultRouter()
router.register(r'images', SentinelImageView, basename='SentinelImage')

urlpatterns = [
    path(r'', include(router.urls)),
]