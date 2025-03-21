from django.urls import path
from .views import *

urlpatterns = [
    path("dataupdate",Master_file_datas.as_view()),
    path("overalldata",Over_all_stats.as_view()),
    path("navdatas",Nav_Datas.as_view())
]