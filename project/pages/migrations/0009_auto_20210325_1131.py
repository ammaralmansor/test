# Generated by Django 3.1.7 on 2021-03-25 09:31

import asgiref.local
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20210325_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dateclass',
            name='created',
            field=models.DateTimeField(default=asgiref.local.Local, verbose_name='Created'),
        ),
    ]
