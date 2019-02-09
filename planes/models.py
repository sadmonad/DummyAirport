from django.db import models


class Plane(models.Model):
    model = models.CharField(max_length=12, db_index=True, unique=True)
    country = models.CharField(max_length=15)
    load_capacity = models.PositiveSmallIntegerField()
    fuel_capacity = models.PositiveSmallIntegerField()
    passengers_capacity = models.PositiveSmallIntegerField(db_index=True)
    description = models.TextField()

    class Meta:
        db_table = 'planes'
