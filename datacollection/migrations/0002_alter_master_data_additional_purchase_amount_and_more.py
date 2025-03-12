# Generated by Django 5.1.6 on 2025-03-10 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datacollection", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="master_data",
            name="additional_purchase_amount",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="amc_active_flag",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="amc_code",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="amc_ind",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="amc_scheme_code",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="channel_partner_code",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="dividend_reinvestment_flag",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="end_date",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="exit_load",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="exit_load_flag",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="face_value",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="isin",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="lock_in_period",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="lock_in_period_flag",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="maximum_purchase_amount",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="maximum_redemption_qty",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="minimum_purchase_amount",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="minimum_redemption_qty",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="purchase_allowed",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="purchase_amount_multiplier",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="purchase_cutoff_time",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="purchase_transaction_mode",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="redemption_allowed",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="redemption_amount_maximum",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="redemption_amount_minimum",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="redemption_amount_multiple",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="redemption_cut_off_time",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="redemption_qty_multiplier",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="redemption_transaction_mode",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="reopening_date",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="rta_agent_code",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="rta_scheme_code",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="scheme_code",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="scheme_name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="scheme_plan",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="scheme_type",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="settlement_type",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="sip_flag",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="start_date",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="stp_flag",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="switch_flag",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="swp_flag",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="master_data",
            name="unique_no",
            field=models.CharField(max_length=100),
        ),
    ]
