# Generated by Django 4.0.5 on 2022-07-05 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0005_rename_product_name_buyproduct_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.PositiveIntegerField(default=0)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('seller_name', models.CharField(max_length=100, null=True)),
                ('seller_price', models.IntegerField(max_length=100, null=True)),
            ],
        ),
    ]