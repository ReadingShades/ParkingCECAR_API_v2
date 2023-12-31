from typing import Optional

from api.models import Detection
from api.serializers import DetectionSerializer
from django.http import Http404, HttpRequest
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class DetectionDetailFileName(APIView):
    """
    Retrieve a list of detection instances matching a given file name.
    """

    @extend_schema(exclude=True)
    def get_objects(self, file_name: str):
        try:
            return Detection.objects.filter(file_name__icontains=file_name)
        except Detection.DoesNotExist as e:
            raise Http404 from e

    @extend_schema(responses=DetectionSerializer)
    def get(
        self,
        request: Optional[HttpRequest],
        file_name: str,
        format=None,
    ):
        detection = self.get_objects(file_name)
        serializer = DetectionSerializer(detection, many=True)
        return Response(
            {"num_coincidences": len(serializer.data), "data": serializer.data},
            status=status.HTTP_200_OK,
        )
