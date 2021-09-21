from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers
from plants_api.models import Plant

class PlantListSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Plant
        exclude = [
            "category",
        ]


class PlantFullSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Plant
        fields = "__all__"
