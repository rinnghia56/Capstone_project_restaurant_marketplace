# Generated by Django 4.2 on 2023-05-27 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0004_openinghour'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='openinghour',
            unique_together={('vendor', 'day')},
        ),
    ]