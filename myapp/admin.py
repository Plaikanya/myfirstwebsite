from django.contrib import admin

##1.Import model ใน myapp มาใช้
from myapp.models import Record

# Register your models here.
#2.ใช้คำสั่ง
admin.site.register(Record)