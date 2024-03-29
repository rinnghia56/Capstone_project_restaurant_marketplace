# Generated by Django 4.2 on 2023-05-20 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_alter_fooditem_category_default'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='foodimagedetails')),
                ('food_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='menu.fooditem')),
            ],
        ),
    ]
