# Generated by Django 4.0.5 on 2022-06-27 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='regmodel',
            name='active',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
