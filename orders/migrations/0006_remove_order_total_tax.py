# Generated by Django 4.2 on 2023-06-09 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_total_data_order_vendors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_tax',
        ),
    ]