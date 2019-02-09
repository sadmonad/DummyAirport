# Generated by Django 2.1.5 on 2019-02-09 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('passengers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_code', models.CharField(db_index=True, max_length=10)),
                ('departure_city', models.CharField(db_index=True, max_length=20)),
                ('arrival_city', models.CharField(db_index=True, max_length=20)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('is_international', models.BooleanField()),
                ('distance', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'flights',
                'ordering': ['departure_time'],
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('flight', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flights.Flight')),
                ('passenger', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='passengers.Passenger')),
            ],
            options={
                'db_table': 'flight_registration',
                'ordering': ['registration_time'],
            },
        ),
    ]
