from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth
from examapp.models import Quetion, Result
# from django.db import connection


def showRemainingTime(request):
       
       request.session['duration'] = request.session['duration'] - 1
       return HttpResponse(request.session['duration'])

def giveMePage1(request):
    return render(request,'examapp/quetionmanagement.html')

def giveMePage2(request):
    return render(request,'examapp/resultanalysis.html')

def giveMePage3(request):
    return render(request,'examapp/admindashboard.html')

def search(request,pageno):
       
    endindex=int(pageno)*3
    startindex=endindex-3

    queryset=Result.objects.filter(subject=request.session['subject'])[startindex:endindex]

    print(queryset)

    count=request.session['count']

    list=[]

    for i in range(0,count):
        list.append(i+1)

    print(list)

    return render(request,'examapp/search.html',{'results':queryset,'listofint':list})
        
    
def search1(request):

     subject=request.GET["subject"]
     request.session['subject']=subject
     noofrecords=Result.objects.filter(subject=subject).count()
     i=noofrecords
     count=0
     
     while i>0:
         count=count+1
         i=i-3
    
     print(f"noofrecords is {noofrecords} and noofpages is {count}")

     request.session['count']=count

     queryset=Result.objects.filter(subject=subject)[0:3]
     print(queryset)

     l=[]
     for i in range(0,count):
        l.append(i+1)
     print(l)

     return render(request,'examapp/search.html',{'results':queryset,'listofint':l})#

# Create your views here.
def startTest(request):
    subjectname=request.GET["subject"]

    request.session["subject"]=subjectname
    queryset=Quetion.objects.filter(subject=subjectname)

    quetionobject=queryset[0]
    return render (request,'examapp/quetion.html',{'quetion':quetionobject})


def nextQuetion(request):

    if 'op' in request.GET:
       dictionary=request.session['answer']
       dictionary[request.GET["qno"]] = [request.GET["qno"],request.GET["qtext"],request.GET["answer"],request.GET["op"]] 
       print(dictionary)
       
    quetionlist=Quetion.objects.filter(subject=request.session["subject"])
    if(request.session["qindex"]<len(quetionlist)-1):
        request.session["qindex"]= request.session["qindex"]+1
        quetionobject=quetionlist[request.session["qindex"]]

        dictionary=request.session["answer"]
        qno=quetionobject.qno
        qno=str(qno)

        if qno in dictionary:
         quetiondet=dictionary[qno]
         previousanswer=quetiondet[3]

        else:
         previousanswer=''
         
        return render (request,'examapp/quetion.html',{'quetion':quetionobject,'previousanswer':previousanswer})
    
    else:
      return render (request,'examapp/quetion.html',{'quetion':quetionlist[len(quetionlist)-1],
      'message':'exam will be completed please click submit'})
          


def previousQuetion(request):

    if 'op' in request.GET:
       dictionary=request.session['answer']
       dictionary[request.GET["qno"]] = [request.GET["qno"],request.GET["qtext"],request.GET["answer"],request.GET["op"]] 
       print(dictionary)

    quetionlist=Quetion.objects.filter(subject=request.session["subject"])
    if(request.session["qindex"]>0):
        request.session["qindex"]= request.session["qindex"]-1
        quetionobject=quetionlist[request.session["qindex"]]

        dictionary=request.session["answer"]
        qno=quetionobject.qno
        qno=str(qno)

        if qno in dictionary:
         quetiondet=dictionary[qno]
         previousanswer=quetiondet[3]

        else:
         previousanswer=''
         
        return render (request,'examapp/quetion.html',{'quetion':quetionobject,'previousanswer':previousanswer})
    
    else:
      return render (request,'examapp/quetion.html',{'quetion':quetionlist[0],
      'message':' please click next  or submit '})
    
def endexam(request):
          
    if 'op' in request.GET:
        
        dictionary=request.session["answer"]

        dictionary[request.GET["qno"]] = [request.GET["qno"],request.GET["qtext"],request.GET["answer"],request.GET["op"]] 

        print(dictionary)

    dictionary=request.session["answer"]

    listoflist=dictionary.values()

     #[ ['1', 'what is module?', 'python file', 'folder'] ,  ['2', 'what is package ?', 'folder', 'folder'] ]

    for list in listoflist:
         if list[2]==list[3]:
             request.session["score"]=request.session["score"]+1
    
    finalscore=request.session["score"]
    username=request.session["username"]
    subjectname=request.session["subject"]
    Result.objects.create(username=username,subject=subjectname,score=finalscore)

    #  print(connection.queries)
    auth.logout(request) # it will remove all keys from session

    return render(request,'examapp/score.html',{'username':username,'score':finalscore,'listoflist':listoflist})



def addQuetion(request):
    quetion=Quetion.objects.create(qno=request.GET['qno'],gtext=request.GET['qtext'],
                    answer=request.GET['answer'],op1=request.GET['op1'],op2=request.GET['op2'],
                    op3=request.GET['op3'],op4=request.GET['op4'],subject=request.GET['subject'])

    return render(request,'examapp/quetionmanagement.html',{'message':'added quetion successfully'})
    
def viewQuetion(request):
    quetion=Quetion.objects.get(qno=request.GET['qno'],subject=request.GET['subject'])
      
    return render(request,'examapp/quetionmanagement.html',{'quetion':quetion})



def updateQuetion(request):
    quetion=Quetion.objects.filter(qno=request.GET['qno'],subject=request.GET['subject']).update(gtext=request.GET['qtext'],
                    answer=request.GET['answer'],op1=request.GET['op1'],op2=request.GET['op2'],
                    op3=request.GET['op3'],op4=request.GET['op4'])

    return render(request,'examapp/quetionmanagement.html',{'message':'updated quetion successfully'})
    

def deleteQuetion(request):
    quetion=Quetion.objects.filter(qno=request.GET['qno'],subject=request.GET['subject'])
    quetion.delete()

    return render(request,'examapp/quetionmanagement.html',{'message':'deleted quetion successfully'})




   