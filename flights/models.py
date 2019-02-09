from django.db import models

from passengers.models import Passenger


class Flight(models.Model):
    flight_code = models.CharField(max_length=10, db_index=True)
    departure_city = models.CharField(max_length=20, db_index=True)
    arrival_city = models.CharField(max_length=20, db_index=True)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    is_international = models.BooleanField()
    distance = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'flights'
        ordering = ['departure_time']

    def __str__(self):
        return f'{self.flight_code}'


class Registration(models.Model):
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
    flight = models.OneToOneField(Flight, on_delete=models.CASCADE)
    registration_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'flight_registration'
        ordering = ['registration_time']

    def __str__(self):
        return f'{self.passenger.full_name} - {self.flight.flight_code}'
