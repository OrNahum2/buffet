# Generated by Django 4.0.6 on 2022-08-03 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooddelivery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='isGlutenFree',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='dish',
            name='isVegeterian',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
