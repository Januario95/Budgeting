from typing import Any, Optional
from django.core.management.base import (
    BaseCommand, CommandError
)
from django.db.models import Sum
from django.utils import timezone
from app.helpers import MONTHS

from app.models import (
    Expense, Month, Type
)
from app.forms import (
    ExpenseForm, ExpenseFilter
)
from app.helpers import MONTHS
import json

class Command(BaseCommand):
    help = 'Generate expenses'

    def handle(self, *args, **options):
        current_year = str(timezone.now().year)
        month = timezone.now().month
        month = MONTHS[month-1]
        current_month = Month.objects.get(name=month[0])
        current_expenses = Expense.objects.filter(
            year=current_year, month=current_month)
        total = current_expenses.aggregate(total=Sum('amount'))
        print(38400 - total.get('total'))


        # expenses = Expense.objects.filter(
        #     expense_type=Type.objects.get(name='Need')
        # )
        # for expense in expenses:
        #     print(expense.serialize())
            # for month in MONTHS[5:]:
                # exp = Expense.objects.create(
                #     name=expense.name,
                #     amount=expense.amount,
                #     expense_type=expense.expense_type,
                #     month=Month.objects.get(name=month[0]),
                #     year='2023'
                # )
                # exp.save()
                # print(json.dumps(exp.serialize(), indent=4, default=str))

        self.stdout.write(
            self.style.SUCCESS('Successfuly generate expenses')
        )