from django.contrib import admin
from .models import Laptop,Login,Student,Subject
# Register your models here.

class LaptopAdmin(admin.ModelAdmin):
    fields = ['company','model','cpu','ram','hdd','price','date']
    list_display = fields
    #list_display_links  = []
    list_editable = ['model','cpu','ram','hdd','price','date']
    search_fields =fields
    list_filter = fields
admin.site.register(Login)
admin.site.register(Student)
admin.site.register(Subject)

admin.site.register(Laptop,LaptopAdmin)
