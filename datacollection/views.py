from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework .response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.pagination import PageNumberPagination
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
        df = pd.read_csv(file_obj, delimiter="|", encoding="utf-8")
        df = df.fillna("")
        df = df.drop(columns=df.columns[df.columns.str.contains("Unnamed")])
        df.columns = ['unique_no', 'scheme_code', 'rta_scheme_code', 'amc_scheme_code', 'isin', 'amc_code', 'scheme_type', 'scheme_plan', 'scheme_name', 'purchase_allowed', 'purchase_transaction_mode', 'minimum_purchase_amount', 'additional_purchase_amount', 'maximum_purchase_amount', 'purchase_amount_multiplier', 'purchase_cutoff_time', 'redemption_allowed', 'redemption_transaction_mode', 'minimum_redemption_qty', 'redemption_qty_multiplier', 'maximum_redemption_qty', 'redemption_amount_minimum', 'redemption_amount_maximum', 'redemption_amount_multiple', 'redemption_cut_off_time', 'rta_agent_code', 'amc_active_flag', 'dividend_reinvestment_flag', 'sip_flag', 'stp_flag', 'swp_flag', 'switch_flag', 'settlement_type', 'amc_ind', 'face_value', 'start_date', 'end_date', 'exit_load_flag', 'exit_load', 'lock_in_period_flag', 'lock_in_period', 'channel_partner_code', 'reopening_date']
        datas = df.to_dict(orient="records")
        master_data.objects.all().delete()
        # for data in datas:
        #     for key, value in data.items():
        #         if isinstance(value, str) and len(value) > 50:
        #             print(f"Field {key} is too long: {value[:100]}")
        data_objects = [master_data(**data) for data in datas]
        master_data.objects.bulk_create(data_objects)
        return Response(
            {
                "msg":"Data updated"
            },status=status.HTTP_200_OK
        )
        
class CustomPagination(PageNumberPagination):
    page_size = 10  # Default page size
    page_size_query_param = 'page_size'  # Allows clients to specify page size
    max_page_size = 100  # Maximum page size allowed
class Over_all_stats(ListCreateAPIView):
    queryset = master_data.objects.all()
    serializer_class = Master_data_serializer
    pagination_class = CustomPagination
        
        
        
