# Generated by Django 3.1.7 on 2021-03-27 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_student_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='User Name')),
                ('password', models.CharField(max_length=50, verbose_name='password')),
            ],
        ),
    ]