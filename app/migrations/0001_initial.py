# Generated by Django 4.2.1 on 2023-05-07 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('expense_type', models.BooleanField(choices=[('need', 'Need'), ('want', 'Want'), ('saving', 'Saving')], default='need')),
                ('month', models.BooleanField(choices=[('january', 'January'), ('february', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'), ('november', 'November'), ('december', 'December')], default='may')),
                ('year', models.CharField(default='2023', max_length=4)),
            ],
        ),
    ]
