# Generated by Django 3.1.7 on 2021-02-22 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='placeholder-food.jpeg', max_length=500),
        ),
    ]
