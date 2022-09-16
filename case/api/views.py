from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from case.api.serializers import GeoJsonSerializer
from case.api.services import ImageService

class SentinelImageView(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = ImageService()

    def list(self, request):
        serializer = GeoJsonSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        user = request.user
        image_id = request.query_params.get('id') 
        data = self.service.get_images(user, image_id, **serializer.validated_data)
        return Response(data, status.HTTP_200_OK)