from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework .response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import MultiPartParser,FormParser
import pandas as pd
# import os

class Master_file_datas(ListCreateAPIView):
    # save_path = "../static/master_datas/"
    queryset = master_data.objects.all()
    serializer_class = Master_data_serializer
    parser_classes = [MultiPartParser, FormParser]
    
    def post(self,request,*agrs,**kwargs):
        file_obj = request.FILES.get("Master_file")
        
        if not file_obj:
            return Response(
                {
                    "msg":"File not uploaded",
                    "error":"No file uploaded"
                },status=status.HTTP_400_BAD_REQUEST
            )
        if not file_obj.name.endswith(".txt"):
            return Response(
                {
                    "error": "Only .txt files are allowed",
                    "msg":"Txt format only acceptable"
                },status=status.HTTP_400_BAD_REQUEST
            )
        df = pd.read_csv(file_obj, delimiter="|", header=None, encoding="utf-8")
        df = df.fillna("")
        datas = df.to_dict(orient="records")
        master_data.objects.bulk_create(datas)
        return Response(
            {
                "msg":"Data updated"
            },status=status.HTTP_200_OK
        )
        
        
        
