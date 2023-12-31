# Generated by Django 4.2.1 on 2023-05-07 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='month',
            name='name',
            field=models.CharField(choices=[('january', 'January'), ('february', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'), ('november', 'November'), ('december', 'December')], default='need', max_length=9),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(choices=[('need', 'Need'), ('want', 'Want'), ('saving', 'Saving')], default='need', max_length=6),
        ),
    ]
