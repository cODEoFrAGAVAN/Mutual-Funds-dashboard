from django.urls import path
from .views import *

urlpatterns = [
    path("dataupdate",Master_file_datas.as_view())
]