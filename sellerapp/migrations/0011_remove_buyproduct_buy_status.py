# Generated by Django 4.0.5 on 2022-07-07 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0010_buyproduct_buy_status_buyproduct_buyer_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyproduct',
            name='buy_status',
        ),
    ]
