from django.db import models
from django.contrib.auth.models import User


class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=12, db_index=True)
    last_name = models.CharField(max_length=15, db_index=True)
    birth_date = models.DateField()
    passport_number = models.CharField(max_length=12, db_index=True)

    class Meta:
        db_table = 'passengers'

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
