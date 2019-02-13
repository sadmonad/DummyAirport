from django.db import models

from planes.models import Plane


class Company(models.Model):
    name = models.CharField(max_length=15, db_index=True, unique=True)
    caption = models.TextField()
    planes = models.ManyToManyField(Plane)

    class Meta:
        db_table = 'companies'
        ordering = ['name']

    def __str__(self):
        return self.name


class ServiceClasses(models.Model):
    SERVICE_LEVELS = (
        ('EC', 'Economy'), ('ST', 'Standart'), ('BS', 'Business')
    )

    company = models.ManyToManyField(Company)
    service_level = models.CharField(max_length=15, choices=SERVICE_LEVELS, db_index=True)
    max_light_baggage_weight = models.PositiveSmallIntegerField()
    max_big_baggage_weight = models.PositiveSmallIntegerField()
    max_baggage_size = models.PositiveSmallIntegerField()
    allow_ticket_return = models.BooleanField(db_index=True)
    price = models.PositiveIntegerField()

    class Meta:
        db_table = 'service_classes'

    def __str__(self):
        return f'{self.company} - {self.service_level}'
