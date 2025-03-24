from .models import *
from rest_framework.serializers import ModelSerializer


class Master_data_serializer(ModelSerializer):
    class Meta:
        model = master_data
        fields = "__all__"
        
class Aum_datas_serializer(ModelSerializer):
    class Meta:
        model = Aum_datas
        fields = "__all__"


class Nav_datas_serializer(ModelSerializer):
    class Meta:
        model = Nav_datas
        fields = "__all__"