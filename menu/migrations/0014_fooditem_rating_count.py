# Generated by Django 4.2 on 2023-06-07 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0013_fooditem_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='rating_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
