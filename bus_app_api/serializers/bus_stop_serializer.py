from rest_framework import serializers
from bus_app_api.models import BusStop


class BusStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusStop
        fields = '__all__'

        def create(self, validated_data):
            return BusStop.create(**validated_data)
    
        def update(self, instance, validated_data):
            instance.part_of_trip = validated_data.get("part_of_trip", instance.part_of_trip)
            instance.stop_name = validated_data.get("stop_name", instance.stop_name)
            instance.bus_arrival_time = validated_data.get("bus_arrival_time", instance.bus_arrival_time)
            instance.save()
            return instance
