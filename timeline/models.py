from django.db import models

from flights.models import Flight


class Timeline(models.Model):
    AWAITING_CHECK_IN = ('AC', 'Awaiting check-in')
    CHECK_IN = ('C', 'Check-in')
    CHECK_IN_OVER = ('CO', 'Check-in is over')
    REJECTED = ('R', 'Rejected')
    DELAYED = ('D', 'Delayed')
    BOARDING = ('B', 'Boarding')
    GATE_CLOSED = ('GC', 'Gate closed')
    IN_FLIGHT = ('F', 'In flight')
    ARRIVED = ('A', 'Arrived')

    FLIGHT_STATUSES = (
        AWAITING_CHECK_IN,
        CHECK_IN_OVER,
        CHECK_IN,
        REJECTED,
        DELAYED,
        BOARDING,
        GATE_CLOSED,
        IN_FLIGHT,
        ARRIVED
    )

    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    terminal = models.CharField(max_length=5)
    flight_status = models.CharField(max_length=20, choices=FLIGHT_STATUSES, default=AWAITING_CHECK_IN, db_index=True)
    gate = models.CharField(max_length=5, null=True, blank=True, db_index=True)

    class Meta:
        db_table = 'timeline'

    def __str__(self):
        return f'{self.flight.flight_code} - {self.flight_status}'
