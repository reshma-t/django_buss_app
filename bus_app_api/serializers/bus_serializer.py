from rest_framework import serializers

from bus_app_api.models import Bus


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'

        def create(self, validated_data):
            return Bus.create(**validated_data)

        def update(self, instance, validated_data):
            instance.bus_name = validated_data.get("bus_name", instance.bus_name)
            instance.bus_reg_no = validated_data.get("bus_reg_no", instance.bus_reg_no)
            instance.save()
            return instance
