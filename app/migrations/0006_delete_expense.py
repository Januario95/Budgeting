# Generated by Django 4.2.1 on 2023-05-07 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_expense_expense_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Expense',
        ),
    ]