# Generated by Django 4.0.6 on 2022-08-03 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooddelivery', '0002_dish_isglutenfree_dish_isvegeterian_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='imageUrl',
            field=models.CharField(max_length=600),
        ),
    ]
