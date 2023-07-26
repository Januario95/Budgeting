from django import forms

from .models import (
    Expense, Month, Type
)

class ExpenseFilter(forms.Form):
    YEARS = (
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
    )
    PRIORITY = (
        ('---------', '---------'),
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    )
    COMPLETED = (
        ('----', '----'),
        ('No', 'No'),
        ('Yes', 'Yes')
    )
    year = forms.ChoiceField(
        choices=YEARS,
        required=True)
    month = forms.ModelChoiceField(
        queryset=Month.objects.all(),
        to_field_name='name',
        required=False,  
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    expense_type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        to_field_name='name',
        required=False,  
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    priority = forms.ChoiceField(
        choices=PRIORITY,
        required=False,  
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    completed = forms.ChoiceField(
        choices=COMPLETED,
        required=False,
        widget=forms.Select(attrs={
            
        }))

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'