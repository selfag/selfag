# Generated by Django 4.0.3 on 2022-06-02 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0014_pensioner_address_pensioner_bps_pensioner_cnic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pensioner',
            name='inc22',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='pensioner',
            name='rest_amount',
            field=models.FloatField(null=True),
        ),
    ]
