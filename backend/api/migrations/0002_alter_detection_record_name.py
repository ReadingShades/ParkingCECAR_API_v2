# Generated by Django 4.2.5 on 2023-10-02 04:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="detection",
            name="record_name",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
