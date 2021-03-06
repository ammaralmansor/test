# Generated by Django 3.1.7 on 2021-03-25 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20210325_1053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dateclass',
            options={},
        ),
        migrations.AddField(
            model_name='dateclass',
            name='time',
            field=models.TimeField(auto_now=True, verbose_name='Time if job'),
        ),
        migrations.AlterField(
            model_name='dateclass',
            name='date',
            field=models.DateField(help_text='Enter your birthday', verbose_name='Birthday Date'),
        ),
    ]
