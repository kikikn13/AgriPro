# Generated by Django 2.1.1 on 2018-11-17 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cultivo_main', '0011_auto_20181116_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='pred_one',
            name='org_mean_Gross_Production_Value_constant_2004_2006_million_US_dollar',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=12),
        ),
    ]