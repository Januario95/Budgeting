from django.urls import path

from .views import (
    add_expense, display_expenses, sort_table,
    delete_expense, charts_view, guide_view,
)

app_name = 'app'

urlpatterns = [
    path('api/sort_table/', sort_table),
    path('api/delete_expense/', delete_expense),

    path('', display_expenses, name='display_expenses'),
    path('guide/', guide_view, name='guide_view'),
    path('charts/', charts_view, name='charts'),
    path('add_expense/', add_expense, name='add_expense'),
]