# Generated by Django 4.2.1 on 2023-05-07 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_expense_month_alter_month_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(choices=[('Need', 'Need'), ('Want', 'Want'), ('Saving', 'Saving')], default='need', max_length=6, unique=True),
        ),
    ]