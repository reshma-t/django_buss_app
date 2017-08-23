from rest_framework import serializers

from bus_app_api.models import Trip


class TripSerializer(serializers.ModelSerializer):
    model = Trip
    fields = '__all__'

    def create(self, validated_data):
        return Trip.create(**validated_data)

    def update(self, instance, validated_data):
        instance.route = validated_data.get("route", instance.route)
        instance.bus = validated_data("bus", instance.bus)
        instance.trip_starting_time = validated_data("trip_starting_time", instance.trip_starting_time)
        instance.save()
        return instance
    