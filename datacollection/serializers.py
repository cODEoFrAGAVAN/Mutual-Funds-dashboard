from .models import *
from rest_framework.serializers import ModelSerializer


class Master_data_serializer(ModelSerializer):
    class Meta:
        model = master_data
        fields = "__all__"
        