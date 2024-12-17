from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.db import connection
from examapp.models import Quetion
from loginapp.models import MyUser
# Create your views here.

def SaveUser(request) :
   if request.method=="GET":
       return render(request,"loginapp/register.html")
   photo=request.FILES['photo']
   imagepath='/upload/'+photo.name

   with open('loginapp/static/upload/'+photo.name, 'wb+') as destination:  
                for byte in photo.chunks():  
                    destination.write(byte)

   MyUser.objects.create_user(username=request.POST['username'],password=request.POST['password'],email=request.POST['email'], imagepath=imagepath)
   
   return render (request,"loginapp/login.html",{})


def login(request):
      if request.method=="GET":  
        return render (request,"loginapp/login.html")
      else:
        userobject=auth.authenticate(username=request.POST["username"],password=request.POST["password"])
        if(userobject.username!='saurabh'):

            print(connection.queries)

            print(userobject)

            print(userobject.id)

            queryset=MyUser.objects.filter(user_ptr_id=userobject.id)

            imagepath=queryset[0].imagepath
            request.session["imagepath"]=imagepath
            print(queryset[0].imagepath)

        if userobject==None:
           return render (request,'loginapp/login.html',{'message':'creditional are not correct'})
        else:
           auth.login(request,userobject) # it will start session
           queryset=Quetion.objects.all().values('subject').distinct()
         
    
           request.session["username"]=userobject.username
           request.session["score"]=0
           request.session["qindex"]=0
           request.session["answer"]={}
           request.session["duration"]=180

           if userobject.is_superuser==0:
            return render (request,"examapp/subject.html",{'queryset':queryset,'imagepath':imagepath})
           else:
              return render (request,"examapp/admindashboard.html")