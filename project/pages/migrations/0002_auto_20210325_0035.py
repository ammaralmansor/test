# Generated by Django 3.1.7 on 2021-03-24 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='company',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='model',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
