# Generated by Django 4.0.3 on 2022-03-09 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0009_alter_pensionincreas_pensioner'),
    ]

    operations = [
        migrations.AddField(
            model_name='pensioner',
            name='inc11',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='pensioner',
            name='inc15',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='pensioner',
            name='inc16',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='pensioner',
            name='inc17',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='pensioner',
            name='inc18',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='pensioner',
            name='inc19',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='pensioner',
            name='inc21',
            field=models.FloatField(null=True),
        ),
        migrations.DeleteModel(
            name='PensionIncreas',
        ),
    ]
