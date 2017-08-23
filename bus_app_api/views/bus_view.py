import logging
from rest_framework.response import Response
from rest_framework.views import APIView

from bus_app_api.models import Bus
from bus_app_api.serializers import bus_serializer


err_logger = logging.getLogger('error_logger')


class BusList(APIView):
    def get(self, request):
        bus = Bus.objects.all()
        return_data = bus_serializer.BusSerializer(bus, many=True)
        return Response(return_data.data)

    def post(self, request):
        serialized_data = bus_serializer.BusSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response("Bus created")
        else:
            err_logger.info(request.data)
            err_logger.error(serialized_data.errors)
            return Response("Cannot create Bus", status=400)


class BusDetail(APIView):

    def get(self, request, pk):
        try:
            bus = Bus.objects.get(pk=pk)
            bus_data = bus_serializer.BusSerializer(bus).data
            status_code = 200
        except Bus.DoesNotExist:
            err_logger.info(request)
            bus_data = None
            status_code = 404
        return Response(bus_data, status=status_code)

    def put(self, request, pk):
        try:
            bus = Bus.objects.get(pk=pk)
            serialised_data = bus_serializer.BusSerializer(bus, data=request.data)
            if serialised_data.is_valid():
                serialised_data.save()
                return Response("Bus updated")
            err_logger.info(request.data)
            err_logger.error(serialised_data.errors)
            return Response(serialised_data.errors, status=400)
        except Bus.DoesNotExist:
            return Response(status=404)

    def delete(self, request, pk):
        try:
            Bus.objects.get(pk=pk).delete()
            return Response("Bus deleted")
        except Bus.DoesNotExist:
            return Response(status=404)
