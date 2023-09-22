# Generated by Django 4.2.5 on 2023-09-22 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_name', models.CharField(max_length=300)),
                ('time_stamp', models.DateTimeField(blank=True, null=True)),
                ('file_name', models.CharField(blank=True, max_length=300, null=True)),
                ('pred_loc', models.CharField(blank=True, max_length=2000, null=True)),
                ('crop_loc', models.CharField(blank=True, max_length=2000, null=True)),
                ('processing_time_pred', models.DecimalField(blank=True, decimal_places=20, max_digits=30, null=True)),
                ('processing_time_ocr', models.DecimalField(blank=True, decimal_places=20, max_digits=30, null=True)),
                ('ocr_text_result', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
