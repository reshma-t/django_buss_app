from rest_framework import serializers

from bus_app_api.models import Route


class RouteSerializer(serializers.ModelSerializer):
    model = Route
    fields = '__all__'

    def create(self, validated_data):
        return Route.create(**validated_data)

    def update(self, ins, validated_data):
        ins.starts_from = validated_data.get("route_starting_point", ins.starts_from)
        ins.ends_at = validated_data.get("ends_at", ins.ends_at)
        ins.save()
        return ins
