from datetime import date
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from course.models import Category

data={
    "Bağış bilgileri":"Bağış bilgileri bilgiler",
    "SERTİFİKA BİLGİLERİ":"SERTİFİKA BİLGİLERİ bilgiler",
    "İŞLEM ÖZETİ":"İŞLEM ÖZETİ bilgiler",
    "ÖDEME BİLGİLERİ":"ÖDEME BİLGİLERİ bilgiler",

}

db={
   "course":[
      {
         "title":"javascript kursu",
         "description":"javascript kurs açıklaması",
         "imageUrl":"",
         "slug":"javascript-kursu",
         "date":date(2022,10,10),
         "isActive":True
      },      
   ],
   "catagories":[
      {"id":1,"name":"Bağış bilgileri","slug":"Bağış bilgileri"},
      {"id":2,"name":"SERTİFİKA BİLGİLERİ","slug":"SERTİFİKA BİLGİLERİ"},
      {"id":3,"name":"İŞLEM ÖZETİ","slug":"İŞLEM ÖZETİ"},
      {"id":4,"name":"ÖDEME BİLGİLERİ","slug":"ÖDEME BİLGİLERİ"},
      ]

}


def index(request):
    kategoriler=Category.objects.all()
    return render(request,'index.html',{
       'categories':kategoriler
    })
   

def details(request,kurs_adı):
    return HttpResponse(f"{kurs_adı}detay sayfassı")

def getCourseByCategory(request,category_name):
   try:
    category_text=Category.objects.all()
    return render(request,'course/course.html',{
       'category':category_name,
       'category_text':category_text
    })
   
   except:
      return HttpResponseNotFound('hatalı giriş yaptının veri tabanında böyle bir veri yok')
def getCourseByCategoryId(request,category_id):
    category_list=list(data.keys())
    if(category_id>len(category_list)):
       return HttpResponseNotFound("yanlış veri istek bilgisi")
    redirect_text=category_list[category_id-1]
    return redirect('/kategori/'+redirect_text)