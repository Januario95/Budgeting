# Generated by Django 4.2.1 on 2023-05-13 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_type_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='priority',
            field=models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Low', max_length=6),
        ),
    ]
