import logging
from rest_framework.response import Response
from rest_framework.views import APIView

from bus_app_api.models import Route
from bus_app_api.serializers import route_serializer


err_logger = logging.getLogger('error_logger')


class RouteList(APIView):

    def get(self, request):
        route_objects = Route.objects.all()
        return_data = route_serializer.RouteSerializer(route_objects, many=True)
        return Response(return_data.data)

    def post(self, request):
        serialized_data = route_serializer.RouteSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response("Route Created")
        else:
            err_logger.info(request.data)
            err_logger.error(serialized_data.errors)
            return Response("Cannot create new Route")


class RouteDetails(APIView):
    def get(self, request, pk):
        try:
            route_object = Route.objects.get(pk=pk)
            response_data = route_serializer.RouteSerializer(route_object)
            return Response(response_data.data)
        except Route.DoesNotExist:
            err_logger.info(request)
            err_logger.error("Route object does not exist")
            return Response(status=404)

    def put(self, request, pk):
        try:
            route_object = Route.objects.get(pk=pk)
            serialised_data = route_serializer.RouteSerializer(route_object, data=request.data)
            if serialised_data.is_valid():
                serialised_data.save()
                return Response("Route Updated")
            else:
                err_logger.info(request)
                err_logger.error(serialised_data.errors)
                return Response(serialised_data.errors)
        except Route.DoesNotExist:
            err_logger.info(request)
            err_logger.error("Route object does not exist")
            return Response(status=404)

    def delete(self, request, pk):
        try:
            Route.objects.get(pk=pk).delete()
            return Response("Route deleted")
        except Route.DoesNotExist:
            err_logger.info(request)
            err_logger.error("Route object does not exist")
            return Response(status=404)

