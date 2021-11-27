from django.shortcuts import render,redirect
from django.contrib import messages
from . models import Detail,Telegram_project,Github_project,Account,File,Message


# Create your views here.
def fun1(request):
    obj_1 = Detail.objects.all()
    obj_2 = Telegram_project.objects.all()
    obj_3 = Github_project.objects.all()
    obj_4 = Account.objects.all()
    obj_5 = File.objects.all()
    return render(request,'index.html',{'object_1':obj_1,'object_2':obj_2,'object_3':obj_3,
                                        'object_4':obj_4,'object_5':obj_5})

def message(request):
    if request.method == "POST":
        username = request.POST['name']
        userEmail = request.POST['email']
        message = request.POST['message']
        msg = Message(username=username,user_mail=userEmail,message=message)
        msg.save()
        messages.info(request, "test")
        return redirect('/')
    return render(request,'index.html')
