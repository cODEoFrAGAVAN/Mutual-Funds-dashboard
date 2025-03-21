from django.db import models

# Create your models here.
# master_data_len = 50
class master_data(models.Model):
    unique_no = models.CharField(max_length=50)
    scheme_code = models.CharField(max_length=50)
    rta_scheme_code = models.CharField(max_length=50)
    amc_scheme_code = models.CharField(max_length=50)
    isin = models.CharField(max_length=50)
    amc_code = models.CharField(max_length=50)
    scheme_type = models.CharField(max_length=50)
    scheme_plan = models.CharField(max_length=50)
    scheme_name = models.CharField(max_length=500)
    purchase_allowed = models.CharField(max_length=50)
    purchase_transaction_mode = models.CharField(max_length=50)
    minimum_purchase_amount = models.CharField(max_length=50)
    additional_purchase_amount = models.CharField(max_length=50)
    maximum_purchase_amount = models.CharField(max_length=50)
    purchase_amount_multiplier = models.CharField(max_length=50)
    purchase_cutoff_time = models.CharField(max_length=50)
    redemption_allowed = models.CharField(max_length=50)
    redemption_transaction_mode = models.CharField(max_length=50)
    minimum_redemption_qty = models.CharField(max_length=50)
    redemption_qty_multiplier = models.CharField(max_length=50)
    maximum_redemption_qty = models.CharField(max_length=50)
    redemption_amount_minimum = models.CharField(max_length=50)
    redemption_amount_maximum = models.CharField(max_length=50)
    redemption_amount_multiple = models.CharField(max_length=50)
    redemption_cut_off_time = models.CharField(max_length=50)
    rta_agent_code = models.CharField(max_length=50)
    amc_active_flag = models.CharField(max_length=50)
    dividend_reinvestment_flag = models.CharField(max_length=50)
    sip_flag = models.CharField(max_length=50)
    stp_flag = models.CharField(max_length=50)
    swp_flag = models.CharField(max_length=50)
    switch_flag = models.CharField(max_length=50)
    settlement_type = models.CharField(max_length=50)
    amc_ind = models.CharField(max_length=50)
    face_value = models.CharField(max_length=50)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    exit_load_flag = models.CharField(max_length=50)
    exit_load = models.CharField(max_length=50)
    lock_in_period_flag = models.CharField(max_length=50)
    lock_in_period = models.CharField(max_length=50)
    channel_partner_code = models.CharField(max_length=50)
    reopening_date = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.isin
    
class Nav_datas(models.Model):
    temp_unique_number = models.IntegerField(primary_key=True,default=0)
    isin = models.CharField(max_length=50)
    aum_in_cr = models.CharField(max_length=50)
    net_expense_ratio = models.CharField(max_length=50)
    nav = models.CharField(max_length=50)
    day_change_in_per = models.CharField(max_length=50)
    week_change_in_per = models.CharField(max_length=50)
    month_change_in_per = models.CharField(max_length=50)    
    ret_in_three_months_per = models.CharField(max_length=50)
    ret_in_one_year_per = models.CharField(max_length=50)
    two_year_cagr = models.CharField(max_length=50)
    three_year_cagr = models.CharField(max_length=50)
    five_year_cagr = models.CharField(max_length=50)
    plan = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.isin