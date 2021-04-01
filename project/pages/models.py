from django.db import models
from django.utils import timezone
import datetime as dt

# Create your models here.


class Laptop(models.Model):
    company_list = [
        ('asus', 'asus'),
        ('lg', 'lg'),
        ('toshiba', 'toshiba'),
        ('acer', 'acer'),
        ('dell', 'dell'),
    ]
    company = models.CharField(max_length=50, null=True, choices=company_list)
    model = models.CharField(max_length=5, blank=True)
    cpu = models.CharField(null=True, max_length=10)
    ram = models.IntegerField()
    hdd = models.CharField(max_length=5)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    test = models.CharField(default='test', null=False, max_length=50)
    image = models.ImageField(upload_to='photo/%y/%m')
    date = models.DateField(default=timezone.now)

    def __str__(self):
        r = self.company + ' ' + self.model
        return r


class Dateclass(models.Model):
    date = models.DateField(("Birthday Date"), auto_now=False,
                            auto_now_add=False, help_text="Enter your birthday")
    time = models.TimeField(
        ("Time if job"), auto_now=False, auto_now_add=False)
    created = models.DateTimeField(
        ("Created"), auto_now=False, auto_now_add=False, default=dt.datetime.now)

    def __str__(self):
        return str(self.date) + ' '+str(self.time)

# one to one


class A(models.Model):
    n = models.CharField(("name"), max_length=50)

    def __str__(self):
        return self.n


class B(models.Model):
    m = models.CharField(("name"), max_length=50)
    nA = models.OneToOneField("A", verbose_name=("g"),
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.m

# one to many


class Product(models.Model):

    title = models.CharField(("title"), max_length=50)

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(("name"), max_length=50, default='name')
    products = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

# many to many


class Subject(models.Model):
    title = models.CharField(("title"), max_length=50)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(("name"), max_length=50,blank=True)
    sub = models.ManyToManyField("Subject", verbose_name=("subjects"))

    def __str__(self):
        return self.name


class Login(models.Model):

    username = models.CharField(("username"), max_length=50)
    password = models.CharField(("password" ), max_length=50)

    def __str__(self):
        return self.username
