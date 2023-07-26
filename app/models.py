from django.db import models
from django.utils import timezone
from django.db.models import Sum

from .helpers import MONTHS

class Type(models.Model):
    TYPES = (
        ('Need', 'Need'),
        ('Want', 'Want'),
        ('Saving', 'Saving')
    )
    name = models.CharField(
        max_length=6,
        unique=True,
        choices=TYPES,
        default='need'
    )

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        ordering = ('id',)
    

class Month(models.Model):
    name = models.CharField(
        max_length=9,
        unique=True,
        choices=MONTHS,
        default='need'
    )

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        ordering = ('id',)

class Expense(models.Model):
    PRIORITY = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    )
    name = models.CharField(max_length=100)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    expense_type = models.ForeignKey(
        to=Type,
        on_delete=models.CASCADE
    )
    month = models.ForeignKey(
        to=Month,
        on_delete=models.CASCADE,
        default=MONTHS[int(timezone.now().strftime('%m'))-1][0]
    )
    year = models.CharField(
        max_length=4,
        default=timezone.now().strftime('%Y')
    )
    priority = models.CharField(
        max_length=6,
        choices=PRIORITY,
        default='Low'
    )
    transaction_day = models.DateField(blank=True)
    completed = models.BooleanField(default=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'amount': self.amount,
            'expense_type': self.expense_type.serialize(),
            'month': self.month.serialize(),
            'year': self.year,
            'priority': self.priority
        }

    def __str__(self):
        return f'{self.name} - {self.expense_type}'

    


