# Generated by Django 2.1.5 on 2019-02-09 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=15, unique=True)),
                ('caption', models.CharField(max_length=100)),
                ('perform_international_flights', models.BooleanField()),
                ('planes', models.ManyToManyField(to='planes.Plane')),
            ],
            options={
                'db_table': 'companies',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ServiceClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_level', models.CharField(choices=[('EC', 'Economy'), ('ST', 'Standart'), ('BS', 'Business')], db_index=True, max_length=15)),
                ('max_light_baggage_weight', models.PositiveSmallIntegerField()),
                ('max_big_baggage_weight', models.PositiveSmallIntegerField()),
                ('max_baggage_size', models.PositiveSmallIntegerField()),
                ('allow_ticket_return', models.BooleanField(db_index=True)),
                ('price', models.PositiveIntegerField()),
                ('company', models.ManyToManyField(to='companies.Company')),
            ],
            options={
                'db_table': 'service_classes',
            },
        ),
    ]
