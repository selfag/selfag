# Generated by Django 3.2.8 on 2022-02-23 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0007_alter_pensioner_qs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pensioner',
            name='doa',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pensioner',
            name='dob',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pensioner',
            name='dor',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
