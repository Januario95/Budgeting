# Generated by Django 4.2.1 on 2023-05-07 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_expense_expense_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='expense_type',
            field=models.BooleanField(choices=[('need', 'Need'), ('want', 'Want'), ('saving', 'Saving')], default='need'),
        ),
    ]
