# Generated by Django 2.1.5 on 2019-02-13 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20190212_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='perform_international_flights',
        ),
    ]
