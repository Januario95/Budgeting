from django.contrib import admin

from .models import (
    Expense, Month, Type
)

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Month)
class MonthAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'amount', 'expense_type', 'transaction_day', 
                    'month', 'year', 'priority', 'completed')
    list_editable = ('name', 'amount', 'transaction_day', 'priority', 'completed')
    list_filter = ('expense_type', 'month', 'year', 'priority')
    search_fields = ('name',)
