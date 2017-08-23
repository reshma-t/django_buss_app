import logging
from rest_framework.response import Response
from rest_framework.views import APIView

from bus_app_api.models import Trip
from bus_app_api.serializers import trip_serializer


err_logger = logging.getLogger('error_logger')


class TripList(APIView):

    def get(self, request):
        trip_objects = Trip.objects.all()
        response_data = trip_serializer.TripSerializer(trip_objects, many=True)
        return Response(response_data.data)

    def post(self, request):
        serialised_data = trip_serializer.TripSerializer(data=request.data)
        if serialised_data.is_valid():
            serialised_data.save()
            return Response("Trip created")
        else:
            err_logger.info(request.data)
            err_logger.error(serialised_data.errors)
            return Response("Trip Cannot be created")


class TripDetails(APIView):
    def get(self, request, pk):
        try:
            trip_objct = Trip.objects.get(pk=pk)
            serialised_data = trip_serializer.TripSerializer(data=trip_objct)
            return Response(serialised_data)
        except Trip.DoesNotExist:
            return Response(status=404)

    def put(self, request, pk):
        try:
            trip_object = Trip.objects.get(pk=pk)
            serialised_data = trip_serializer.TripSerializer(trip_object, data = request.data)
            if serialised_data.is_valid():
                serialised_data.save()
                return Response("Trip updated")
            else:
                err_logger.info(request.data)
                err_logger.error(serialised_data.errors)
                return Response(serialised_data.errors)
        except Trip.DoesNotExist:
            return Response("Trip not Found", status=404)

    def delete(self, request, pk):
        try:
            Trip.objects.get(pk=pk).delete()
            return Response("Trip deleted")
        except Trip.DoesNotExist:
            return Response("Trip not found", status=404)

