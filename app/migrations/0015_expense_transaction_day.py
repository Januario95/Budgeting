# Generated by Django 4.2.1 on 2023-05-22 19:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_expense_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='transaction_day',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
