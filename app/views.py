from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.db.models import Sum

from .models import (
    Expense, Month, Type
)
from .forms import (
    ExpenseForm, ExpenseFilter
)
from .helpers import MONTHS
import json
from datetime import datetime

@require_POST
def delete_expense(request):
    data = json.loads(request.body)
    print(data)
    pk = int(data.get('pk'))
    delete_code = data.get('delete_code')

    correct_code = False
    if delete_code == '4207':
        expense = Expense.objects.filter(pk=pk)
        if expense.exists():
            expense = expense.first()
            expense.delete()
            correct_code = True

    return JsonResponse({
        'correct_code': correct_code
    })

def get_total(expenses):
    value = expenses.aggregate(total=Sum('amount'))
    return value['total']

@require_POST
def sort_table(request):
    data = json.loads(request.body)
    value = data.get('value')
    month = data.get('month')
    year = data.get('year')
    expense_type = data.get('expense_type')
    priority = data.get('priority')
    completed = data.get('completed')
    print(f'completed = {completed}')
    
    expenses = Expense.objects.filter(
        year=year
    )
    if month != '':
        expenses = expenses.filter(
            month=Month.objects.get(name=month)
        )
    if expense_type != '':
        expenses = expenses.filter(
            expense_type=Type.objects.get(name=expense_type)
        )
    if priority != '---------':
        expenses = expenses.filter(
            priority=priority
        )
    if completed != '----':
        if completed == 'Yes':
            expenses = expenses.filter(
                completed=True
            )
        if completed == 'No':
            expenses = expenses.filter(
                completed=False
            )

    expenses = expenses.order_by(value)
    total = get_total(expenses)
    expenses_ = []
    for expense in expenses:
        expenses_.append(expense.serialize())

    return JsonResponse({
        'data': expenses_,
        'total': total
    })


def guide_view(request):
    expenses = current_month_expenses()
    total_expenses = expenses.aggregate(total=Sum('amount'))
    needs = expenses.filter(
        expense_type=Type.objects.get(name='Need'))
    total_needs = needs.aggregate(total=Sum('amount'))
    wants = expenses.filter(
        expense_type=Type.objects.get(name='Want'))
    total_wants = wants.aggregate(total=Sum('amount'))
    savings = expenses.filter(
        expense_type=Type.objects.get(name='Saving'))
    total_savings = savings.aggregate(total=Sum('amount'))

    return render(request,
                  'app/guide.html',
                  {'total_needs': total_needs, 'total_wants': total_wants,
                   'total_savings': total_savings, 'total_expenses': total_expenses})

def current_month_expenses():
    now = datetime.now()
    expenses = Expense.objects.filter(
        month=Month.objects.get(name=MONTHS[now.month-1][0]),
        year='2023').order_by('name')
    return expenses
    

def charts_view(request):
    expenses = current_month_expenses()
    total_expenses = expenses.aggregate(total=Sum('amount'))
    needs = expenses.filter(
        expense_type=Type.objects.get(name='Need'))
    total_needs = needs.aggregate(total=Sum('amount'))
    wants = expenses.filter(
        expense_type=Type.objects.get(name='Want'))
    total_wants = wants.aggregate(total=Sum('amount'))
    savings = expenses.filter(
        expense_type=Type.objects.get(name='Saving'))
    total_savings = savings.aggregate(total=Sum('amount'))

    form = ExpenseFilter()

    return render(request,
                  'app/charts.html',
                  {'form': form,
                   'total_needs': total_needs, 'total_wants': total_wants,
                   'total_savings': total_savings, 'total_expenses': total_expenses})

def display_expenses(request):
    expenses = current_month_expenses()
    total_expenses = expenses.aggregate(total=Sum('amount'))
    needs = expenses.filter(
        expense_type=Type.objects.get(name='Need'))
    total_needs = needs.aggregate(total=Sum('amount'))
    wants = expenses.filter(
        expense_type=Type.objects.get(name='Want'))
    total_wants = wants.aggregate(total=Sum('amount'))
    savings = expenses.filter(
        expense_type=Type.objects.get(name='Saving'))
    total_savings = savings.aggregate(total=Sum('amount'))
    total = get_total(expenses)
    if request.method == 'POST':
        form = ExpenseFilter(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            year = data.get('year')
            month = data.get('month')
            expense_type = data.get('expense_type')
            priority = data.get('priority')
            completed = data.get('completed')
            expenses = Expense.objects.filter(
                year=year
            )
            if (month is None and expense_type is None and 
                priority == '---------' and completed == '----'):
                pass
            else:
                if expense_type is not None:
                    expenses = expenses.filter(
                        expense_type=expense_type
                    )
                if month is not None:
                    expenses = expenses.filter(
                        month=month
                    )
                if priority != '---------':
                    expenses = expenses.filter(
                        priority=priority
                    )
                if completed == 'Yes':
                    expenses = expenses.filter(
                        completed=True
                    )
                if completed == 'No':
                    expenses = expenses.filter(
                        completed=False
                    )
                # print(expenses)
            total = get_total(expenses)
        else:
            print(form.errors)
    else:
        form = ExpenseFilter()

    print(f'total = {total}')

    return render(request,
                  'app/display_expenses.html',
                  {'expenses': expenses, 'form': form,
                   'total_needs': total_needs, 'total_wants': total_wants,
                   'total_savings': total_savings, 'total_expenses': total_expenses,
                   'total': total})

def add_expense(request):
    expenses = current_month_expenses()
    total_expenses = expenses.aggregate(total=Sum('amount'))
    needs = expenses.filter(
        expense_type=Type.objects.get(name='Need'))
    total_needs = needs.aggregate(total=Sum('amount'))
    wants = expenses.filter(
        expense_type=Type.objects.get(name='Want'))
    total_wants = wants.aggregate(total=Sum('amount'))
    savings = expenses.filter(
        expense_type=Type.objects.get(name='Saving'))
    total_savings = savings.aggregate(total=Sum('amount'))

    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            form = ExpenseForm()
        else:
            print(form.errors)
    else:
        form = ExpenseForm()

    return render(request,
                  'app/add_expense.html',
                  {'form': form, 'total_needs': total_needs, 'total_wants': total_wants,
                   'total_savings': total_savings, 'total_expenses': total_expenses})