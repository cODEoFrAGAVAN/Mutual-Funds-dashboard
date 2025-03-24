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
from io import StringIO
import traceback
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



class Aum_datas(ListCreateAPIView):
    queryset = Aum_datas.objects.all()
    serializer_class = Aum_datas_serializer
    
    def fetch_and_store_aum_data(self):
        Aum_datas.objects.all().delete()
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

        # data_objects = []
        print(" :: Trendy data :: ")
        main_df = pd.DataFrame()
        for item in list1:
            for plan in list2:
                print("loading...")
                url = f"https://trendlyne.com/mutual-fund/getMFdata/?category={item}&plan={plan}"
                # print("url :: ",url)
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
                    if len(datas) < 6:
                        print(" :: url :: ",url," :: skipped :: ")
                        continue  # Ensure sufficient data
                    sub_list1 = [
                        datas[0].get("isin", ""),
                        datas[0].get("name",""),
                        datas[5] if datas[5] else "",
                        datas[6] if datas[6] else "",
                        # datas[7] if datas[7] else "",
                        # datas[8] if datas[8] else "",
                        # datas[9] if datas[9] else "",
                        # datas[10] if datas[10] else "",
                        # datas[11] if datas[11] else "",
                        # datas[12] if datas[12] else "",
                        # datas[13] if datas[13] else "",
                        # datas[14] if datas[14] else "",
                        # datas[15] if datas[15] else "",
                        datas[-2] if datas[-2] else "",
                        datas[-1] if datas[-1] else "",
                        plan,
                        item.replace("%26", "&").replace("+", " ")  # Fix category string
                    ]
                    data_list.append(sub_list1)

                df = pd.DataFrame(data_list, columns=[
                    "isin","src_name","aum_in_cr", "net_expense_ratio","three_year_cagr",
                    "five_year_cagr", "plan", "category"])
                df = df.fillna("")
                df = df.astype(str)
                df = df.reset_index(drop=True)
                # df["temp_unique_number"] = ""
                # print("df.columns :: ",df.columns)
                # for index,row in df.iterrows():
                #     df.loc[index,"temp_unique_number"] = int(index)+1
                # datas1 = df.to_dict(orient="records")
                # print(datas1[0])
                # data_objects.append([Nav_datas(**data) for data in datas1])
                # if data_objects:
                #     Nav_datas.objects.bulk_create(data_objects)
                main_df = pd.concat([main_df,df],axis=0,ignore_index=True)
                # time.sleep(1)
            # time.sleep(1)# Avoid rapid API hits
        main_df["temp_unique_number"] = 0
        for index,row in main_df.iterrows():
            main_df.loc[index,"temp_unique_number"] = int(index)+1
        datas1 = main_df.to_dict(orient="records")
        data_objects = [Aum_datas(**data) for data in datas1]
        if data_objects:
            Aum_datas.objects.bulk_create(data_objects)

        return {"msg": "Data updated"}

    def post(self, request, *args, **kwargs):
        result = self.fetch_and_store_aum_data()
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
        
        
class Nav_Datas(ListCreateAPIView):
    queryset = Nav_datas.objects.all()
    serializer_class = Nav_datas_serializer

    def fetch_and_store_nav_data(self):
        try:
            Nav_datas.objects.all().delete()
        except:
            pass

        url = "https://www.amfiindia.com/spages/NAVAll.TXT"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload, timeout=20)
        print("Response Done")
        df = pd.read_csv(StringIO(response.text), delimiter=";")
        df.columns = [
            "scheme_code",
            "isin",
            "isin_div_reinversment",
            "scheme_name",
            "nav",
            "dates",
        ]
        df = df.astype(str)
        df["temp_unique_number"] = 0
        for index,row in df.iterrows():
            df.loc[index,"temp_unique_number"] = int(index)+1
        datas = df.to_dict(orient="records")
        data_objects = [Nav_datas(**i)for i in datas]
        if data_objects:
            Nav_datas.objects.bulk_create(data_objects)
        return {"msg": "Data updated"}
    def post(self,request,*args,**kwargs):
        try:
            result = self.fetch_and_store_nav_data()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(" Error :: ",e)
            print("traceback :: ",traceback.format_exc())
            return Response("Error")
        


