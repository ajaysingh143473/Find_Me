# Generated by Django 4.2.7 on 2024-02-06 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_remove_finepage_latitude_remove_finepage_longitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='finepage',
            name='elec',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='finepage',
            name='fash',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='finepage',
            name='homefurt',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
