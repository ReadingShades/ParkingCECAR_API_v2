import logging
import uuid

from api.models import Detection
from api.serializers import DetectionSerializer
from api.tasks import background_detection
from core import celery_utils
from detector_utils import detector_interface
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class DetectionList(APIView):
    """
    List all detections, or create a new detection.
    """

    def get(self, request, format=None):
        detections = Detection.objects.all()
        serializer = DetectionSerializer(detections, many=True)
        return Response(
            {"total": len(serializer.data), "data": serializer.data},
            status=status.HTTP_200_OK,
        )

    def post(self, request, format=None):
        data = request.data

        id_field = uuid.uuid4()

        worker_status = celery_utils.get_worker_status()
        # print(f"Testing worker status: {worker_status}")
        worker_availability = worker_status.get("availability")
        # print(f"Testing worker availability: {worker_availability}")
        worker_up_flag = False
        if worker_availability is not None:
            if len(worker_availability) > 0:
                background_detection.delay(id_field, data)
                worker_up_flag = True
        else:
            logging.warning("Celery-redis worker down")

        if not worker_up_flag:
            self.detector_funtion(id_field, data)

        payload = {}
        payload["id_ref"] = id_field
        payload[
            "msg"
        ] = "Check back with that uuid in 30 secs at the endpoint /detections/ref/<uuid:id_ref>"

        return Response(payload, status=status.HTTP_201_CREATED)

    def detector_funtion(self, id_field, data):
        detector_ins = detector_interface.Detector()
        payload = detector_ins.detect_license_from_fs_location(
            fs_location=data["data"]["src_file"]
        )
        payload["detection"]["id_ref"] = id_field
        # print(f"payload: {payload}")
        serializer = DetectionSerializer(data=payload.get("detection"))
        """ print("1. validity--------------------------------")
        print(f"serializer: valid? {serializer.is_valid()}")
        print("2. errors  --------------------------------")
        print(serializer.errors)
        print("3. data    --------------------------------")
        print(serializer.validated_data)
        print("-------------------------------------------") """
        if serializer.is_valid(raise_exception=True):
            serializer.save()