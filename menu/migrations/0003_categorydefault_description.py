# Generated by Django 4.2 on 2023-05-19 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_categorydefault_fooditem_category_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorydefault',
            name='description',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]