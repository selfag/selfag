# Generated by Django 3.2.8 on 2022-03-08 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0007_alter_pensionincreas_pensioner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pensionincreas',
            name='pensioner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pms.pensioner'),
        ),
    ]
