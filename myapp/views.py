from django.shortcuts import render,redirect
from django.http import HttpResponse #เป็นการบอกว่าให้ทำการแสดงข้อมูลที่หน้าเว็บไซต์
from myapp.models import Record #Impoer model เข้ามาเพื่อทำการดึงฐานข้อมูลมาใใช้
from django.contrib import messages #เรียกใช้การแจ้งเตือนข้อความ pop up ตอบกลับลูกค้า
# Create your views here.
def index(request) :
    #ทำการดึงข้อมูลจากหน้า Class record ใน Model มาใช้ในการแสดงผล
    all_record = Record.objects.all()
    return render(request,"index.html" , {"all_record" : all_record})

def about(request) :
    return render(request, "about.html")

def form(request) :
    if request.method == "POST" :
        ##รับข้อมูลเข้ามาใน view
        name = request.POST["name"] 
        age = request.POST["age"]
        
        ##บันทึกข้อมูล
        record = Record.objects.create(
            name = name , ##Feild name ให้ดึงข้อมูลมาจากตัวแปร Name
            age = age
        )
        record.save() #ทำการบันทึกข้อมูลงฐานข้อมูล

        #pop up ข้อความ
        messages.success(request , "Complete")
        #กำหนดตำแหน่งให้ pop up ที่ form.html

        ##เปลี่ยนเส้นทาง
        return redirect("/form") ##คำสั่งว่าหลังจากส่งข้อมูลมาแล้วให้กลับไปที่ path form

    else :
        return render(request,"form.html")

##สร้างFunction ในการแก้ไขข้อมูล
def edit(request , i_id):
    ##ใช้ If ตรวจสอบว่ามีการส่งข้อมูลมาหรือไม่
    if request.method == "POST" :
        i = Record.objects.get(id = i_id) ##ตรวจว่าข้อมูลที่ส่งมาใหม่อยู่ใน id อะไร
        i.name = request.POST["name"] ##ข้อมูลใหม่จะถูกส่งกลับไป update ที่ตาราง
        i.age = request.POST["age"]
        i.save()
        messages.success(request , "Information has been updated")
        return redirect("/")

    else :
        i = Record.objects.get(id = i_id) ##ดึงข้อมูลประชากรที่ต้องการแก้ไข
        return render(request , "edit.html" , {"i" : i})

##สร้าง Function ในการ delet
def delet(request , i_id):
    i = Record.objects.get(id = i_id)
    i.delete()
    messages.success(request , "Information has been deleted")
    return redirect("/")

# ตัวเก่า
#def index(request) :
    #name = "Admin" #สร้างตัวแปรเพิ่มเพื่อให้ไปแสดงที่หน้าเว็บ
    #age = 15
    #return render(request,"index.html" , {"name" : name , "age" : age})

#def about(request) :
    #return render(request, "about.html")

#def form(request) :
    #return render(request,"form.html")