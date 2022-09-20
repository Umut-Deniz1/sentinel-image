from django.urls import include, path
from rest_framework import routers
from case.api.views import SentinelImageView

app_name = 'api'

router = routers.DefaultRouter()
router.register('images', SentinelImageView, basename='SentinelImage')

urlpatterns = [
    path(r'', include(router.urls)),
]