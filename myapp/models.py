from django.db import models

# Create your models here.
#ทำการเรียก class แม่มาใช่เนื่องจากเราอาศัย database Django 
class Record(models.Model) :
    #ทำการสร้างตัวแปรเพื่อเก็บชื่อ ซึ่งเป็นการเก็บข้อมูลในรูปแบบตัวอักษร โดยในวงเล็บเป็นการบอกจำนวนความยาวคำที่จะให้รับเข้ามาสูงสุด 100 ตัวอักษร
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    #สร้าง Function เพื่อให่แสดงข้อมูที่กรอกไว้ ณ หน้าเว็บไซต์
    def __str__(self) :
        return self.name