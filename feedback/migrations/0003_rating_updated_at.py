# Generated by Django 4.2 on 2023-06-06 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]