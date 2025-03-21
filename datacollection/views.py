from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework .response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.pagination import PageNumberPagination
import pandas as pd
import requests,time
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
        
        
# class Nav_datas(ListCreateAPIView):
#     queryset = Nav_data.objects.all()
#     serializer_class = Nav_data_serializer
    
#     def nav_api(self):
#         list1 = [
#             "Multi+%26+Flexi-Cap",
#             "Large-Cap",
#             "Large+%26+Mid-Cap",
#             "Mid-Cap",
#             "Small-Cap",
#             "ELSS",
#             "Dividend+Yield",
#             "Equity+-+Sectoral",
#             "Contra",
#             "Focused+Fund",
#             "Value",
#             "RGESS",
#             "Equity+-+Other",
#             "Fund of Funds",
#             "Index Funds",
#             "Global - Other",
#             "Children",
#             "Retirement",
#             "Low Duration",
#             "Short Duration",
#             "Medium Duration",
#             "Medium to Long Duration",
#             "Long Duration",
#             "Dynamic Bond",
#             "10 yr Government Bond",
#             "Government Bond",
#             "Corporate Bond",
#             "Credit Risk",
#             "Floating Rate",
#             "Banking %26 PSU",
#             "Ultra Short Duration",
#             "Liquid",
#             "Money Market",
#             "Overnight",
#             "Aggressive Allocation",
#             "Arbitrage Fund",
#             "Dynamic Asset Allocation",
#             "Multi Asset Allocation",
#             "Conservative Allocation",
#             "Balanced Allocation",
#         ]
#         list2 = ["Direct","Regular"]

#         for item in list1:
#             for plan in list2:
#                 url = "https://trendlyne.com/mutual-fund/getMFdata/?category={}&plan={}".format(item,plan)

#                 payload = {}
#                 headers = {
#                 'Cookie': 'csrftoken=sYR4IBVMBqmNAD8Ienyfkwnyb5dZUGUyVMCqqaSh2DWwMYnIMLIfJlDPi2FP4mlj'
#                 }

#                 response = requests.request("GET", url, headers=headers, data=payload,timeout=10)
#                 _json = response.json()
#                 data_list = list()
#                 for datas in _json["body"]["tableData"]:
#                     sub_list1 = list()
#                     sub_list1.append(datas[0]["isin"] if datas[0]["isin"] else "")
#                     sub_list1.append(datas[5:])
#                     data_list.append(sub_list1)
#                 df = pd.DataFrame(data_list)
#                 df.columns = ["isin","aum_in_cr","net_expense_ratio","nav","day_change_in_per","week_change_in_per","month_change_in_per","ret_in_three_months_per","ret_in_one_year_per","two_year_cagr","five_year_cagr","plan","category"]
#                 df["category"] = df["category"].str.replace("%26","").replace("+","")
#                 datas = df.to_dict(orient="records")
#                 data_objects = [Nav_data(**data) for data in datas]
#                 Nav_data.objects.bulk_create(data_objects)
#                 time.sleep(5)
#         return Response(
#             {
#                 "msg":"Data updated"
#             },status=status.HTTP_200_OK
#         )



class Nav_Datas(ListCreateAPIView):
    queryset = Nav_datas.objects.all()
    serializer_class = Nav_data_serializer
    
    def fetch_and_store_nav_data(self):
        Nav_datas.objects.all().delete()
        list1 = [
            "Multi+%26+Flexi-Cap",
            "Large-Cap",
            "Large+%26+Mid-Cap",
            "Mid-Cap",
            "Small-Cap",
            "ELSS",
            "Dividend+Yield",
            "Equity+-+Sectoral",
            "Contra",
            "Focused+Fund",
            "Value",
            "RGESS",
            "Equity+-+Other",
            "Fund of Funds",
            "Index Funds",
            "Global - Other",
            "Children",
            "Retirement",
            "Low Duration",
            "Short Duration",
            "Medium Duration",
            "Medium to Long Duration",
            "Long Duration",
            "Dynamic Bond",
            "10 yr Government Bond",
            "Government Bond",
            "Corporate Bond",
            "Credit Risk",
            "Floating Rate",
            "Banking %26 PSU",
            "Ultra Short Duration",
            "Liquid",
            "Money Market",
            "Overnight",
            "Aggressive Allocation",
            "Arbitrage Fund",
            "Dynamic Asset Allocation",
            "Multi Asset Allocation",
            "Conservative Allocation",
            "Balanced Allocation",
        ]
        list2 = ["Direct", "Regular"]

        data_objects = []
        
        for item in list1:
            for plan in list2:
                url = f"https://trendlyne.com/mutual-fund/getMFdata/?category={item}&plan={plan}"
                
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                }

                try:
                    response = requests.get(url, headers=headers, timeout=10)
                    response.raise_for_status()
                    _json = response.json()
                except requests.exceptions.RequestException as e:
                    print(f"Request failed for {url}: {e}")
                    continue
                except ValueError:
                    print(f"Invalid JSON response for {url}")
                    continue

                if "body" not in _json or "tableData" not in _json["body"]:
                    print(f"Missing expected keys in response for {url}")
                    continue

                data_list = []
                for datas in _json["body"]["tableData"]:
                    pr
                    if len(datas) < 6:
                        continue  # Ensure sufficient data
                    sub_list1 = [
                        datas[0].get("isin", ""),
                        datas[5],
                        datas[6],
                        datas[7],
                        datas[8],
                        datas[9],
                        datas[10],
                        datas[11],
                        datas[12],
                        datas[13],
                        datas[14],
                        plan,
                        item.replace("%26", "&").replace("+", " ")  # Fix category string
                    ]
                    data_list.append(sub_list1)

                df = pd.DataFrame(data_list, columns=[
                    "isin", "aum_in_cr", "net_expense_ratio", "nav", "day_change_in_per", "week_change_in_per",
                    "month_change_in_per", "ret_in_three_months_per", "ret_in_one_year_per", "two_year_cagr","three_year_cagr",
                    "five_year_cagr", "plan", "category"
                ])
                df = df.fillna("")
                df = df.astype(str)
                df = df.reset_index(drop=True)
                df["temp_unique_number"] = ""
                print("df.columns :: ",df.columns)
                for index,row in df.iterrows():
                    df.loc[index,"temp_unique_number"] = int(index)+1
                datas1 = df.to_dict(orient="records")
                print(datas1[0])
                data_objects.append([Nav_datas(**data) for data in datas1])
                if data_objects:
                    Nav_datas.objects.bulk_create(data_objects)
                time.sleep(5)
            time.sleep(5)# Avoid rapid API hits

        return {"msg": "Data updated"}

    def post(self, request, *args, **kwargs):
        result = self.fetch_and_store_nav_data()
        return Response(result, status=status.HTTP_200_OK)

class CustomPagination(PageNumberPagination):
    page_size = 10  # Default page size
    page_size_query_param = 'page_size'  # Allows clients to specify page size
    max_page_size = 100  # Maximum page size allowed
class Over_all_stats(ListCreateAPIView):
    # queryset = master_data.objects.all()
    serializer_class = Master_data_serializer
    pagination_class = CustomPagination
    
    def get_queryset(self):
        queryset = master_data.objects.all()
        request = self.request
        
        funds:str = request.query_params.get("funds","")
        if funds:
            queryset = queryset.filter(scheme_plan=funds.upper())
        return queryset        
        
        
