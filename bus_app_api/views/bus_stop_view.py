import logging
from rest_framework.response import Response
from rest_framework.views import APIView

from bus_app_api.models import BusStop
from bus_app_api.serializers import bus_stop_serializer


err_logger = logging.getLogger('error_logger')


class BusStopList(APIView):

    def get(self, request):
        bus_stop = BusStop.objects.all()
        serialised_data = bus_stop_serializer.BusStopSerializer(bus_stop, many=True)
        return Response(serialised_data.data)

    def post(self, request):
        serilised_data = bus_stop_serializer.BusStopSerializer(data=request.data)
        if serilised_data.is_valid():
            serilised_data.save()
            return Response("Bus Stop Created")
        else:
            err_logger.info(request.data)
            err_logger.error(serilised_data.errors)
            return Response(serilised_data.errors, status=400)


class BusStopDetails(APIView):

    def get(self, request, pk):
        try:
            bus_stop = BusStop.objects.get(pk=pk)
            serialised_data = bus_stop_serializer.BusStopSerializer(data=bus_stop)
            return Response(serialised_data)
        except BusStop.DoesNotExist:
            err_logger.info(request)
            err_logger.error("Bus stop not found")
            return Response("Bus stop not found", status=404)

    def put(self, request, pk):
        try:
            bus_stop = BusStop.objects.get(pk=pk)
            serialised_data = bus_stop_serializer.BusStopSerializer(bus_stop, data = request.data)
            if serialised_data.is_valid():
                serialised_data.save()
                return Response("Bus stop data updated")
            else:
                err_logger.info(request)
                err_logger.error(serialised_data.errors)
                return Response(serialised_data.errors)
        except BusStop.DoesNotExist:
            err_logger.info(request)
            err_logger.error("Bus stop does not exist")
            return Response(status=404)

    def delete(self, request, pk):
        try:
            BusStop.objects.get(pk=pk).delete()
            return Response("Bus stop deleted")
        except BusStop.DoesNotExist:
            err_logger.info(request)
            err_logger.error("Bus stop does not exist")
            return Response(status=404)
