# Generated by Django 4.0.3 on 2022-06-23 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0017_alter_pensioner_restd'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Increase',
        ),
        migrations.AddField(
            model_name='pensioner',
            name='cat',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pensioner',
            name='dobf',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='pensioner',
            name='fpname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pensioner',
            name='incm',
            field=models.FloatField(null=True),
        ),
    ]