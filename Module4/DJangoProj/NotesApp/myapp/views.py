import random

import requests  # sms otp text msg
from django.contrib import messages  # view to template msg viewing
from django.contrib.auth import logout
from django.core.mail import send_mail  # email
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.urls import is_valid_path

from NotesApp import settings

from .forms import *  # UserSignUpForm,mynotesForm,feedbackForm
from .models import *  # UserSignUp,mynotes,feedback


# Create your views here.
def index(request):
    if request.method=='POST':
        # print("post request")
        # print(request.POST.get('signup'))
        if request.POST.get('signup')=='signup':
            username=""
            newuser=UserSignUpForm(request.POST)
            if newuser.is_valid():
                username=newuser.cleaned_data.get("UNm")
                
                try:
                    unm=UserSignUp.objects.get(UNm=username)
                    print("User Name already Exists")
                except UserSignUp.DoesNotExist:
                    newuser.save()
                    return redirect('/') # url path name
            else:
                print(newuser.errors)
        elif request.POST.get("signin")=='signin':#button submit event request.get/post
            username=request.POST["UNm"] #request.post
            password=request.POST["PWD"]
            request.session["user"]=username
            user=UserSignUp.objects.filter(UNm=username,PWD=password)
            # request.session["uid"]=UserSignUp.objects.get()
            if user: #true
                print("Login Sucessful..")
                return redirect("notes")
            else:
                # print("Error Plz Try Again")
                messages.error(request,"Error- Check Username /Password..")
    return render(request,'index.html')

def notes(request):
    user=request.session.get("user")
    # if not request.user.is_authenticated:
    #          return HttpResponseRedirect('/')
    if request.method=='POST':
        notesobj=mynotesForm(request.POST,request.FILES)#File Request do write capital POST AND FILES
        if notesobj.is_valid():
            notesobj.save()
            print("Your notes has been uploaded sucessfully")
            return HttpResponseRedirect("/notes")
        else:
            print(notesobj.errors)
    return render(request,'notes.html',{'user':user})

def userLogout(request):
    logout(request)
    return redirect("/")

def updateProfile(request):
    user=request.session.get("user")
    cuser=UserSignUp.objects.get(UNm=user)
    # uid=request.session.get('userid')
    # user=request.session.get('user')
    # cuser=userSignup.objects.get(id=uid)
    # print("Inside Update Profile")
    # print(cuser.id)
    if request.method=='POST':
        updateuser=UserSignUpForm(request.POST)
        if updateuser.is_valid():
            updateuser=UserSignUpForm(request.POST,instance=cuser)
            updateuser.save()
            return HttpResponseRedirect("/updateProfile")
            print("User Profile has been sucessfully Updated")
        else:
            print(updateuser.errors)
    return render(request,'updateProfile.html',{'cuser':cuser})

def about(request):
    return render(request,'about.html')

def contact(request):
    #user=request.session.get("user")
    if request.method=='POST':
        sendfeedback=feedbackForm(request.POST)
        if sendfeedback.is_valid():
            sendfeedback.save()
            #Email Send Code
            user=request.session.get("user")
            FeedbackUser=request.POST["email"]
            mobile=request.POST["mobile"]
            # subject = 'Thanks For Writing to Us!'
            # message = f'Hi {FeedbackUser},\n\n Thank u for Visiting our Website and giving ur Valuable FeedBack.\n\nThank & Regards {user}'
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list =['dishu.vora@gmail.com','dvjain0584@gmail.com']
            # send_mail(subject=subject,message=message,from_email=email_from,recipient_list=recipient_list)

            #otp Sending using fast2sms
            # otp=random.randint(55555,99999)
            # url = "https://www.fast2sms.com/dev/bulkV2"

            # querystring = {"authorization":"PSqGhvu5BkQv1WEvvWH6PIgV0vr1IcOIEzgsN1fZMHFG0WJapJ1hGGIwYfq8","variables_values":f"{otp}","route":"otp","numbers":"9879316741"}

            # headers = {
            #     'cache-control': "no-cache"
            # }

            # response = requests.request("GET", url, headers=headers, params=querystring)

            # print(response.text)

            #quick sms sendin using fast2sms
            # url = "https://www.fast2sms.com/dev/bulkV2"

            # querystring = {"authorization":"PSqGhvu5BkQv1WEvvWH6PIgV0vr1IcOIEzgsN1fZMHFG0WJapJ1hGGIwYfq8","message":f"Dear {FeedbackUser} Thanks for giving your Valueable Feedback!\n\n Thanks & Regards {user}","language":"english","route":"q","numbers":f"{mobile}"}

            # headers = {
            #     'cache-control': "no-cache"
            # }

            # response = requests.request("GET", url, headers=headers, params=querystring)

            # print(response.text)
            # messages.success(request,"FeedBack Submitted Sucessfully")
            print("Your Feedback has been submitted Please Check your Email for Confirmation")
            return HttpResponseRedirect("/contact") #To avoid form submission need to redirect to another page
        else:
            print(sendfeedback.errors)
    return render(request,'contact.html')#,{"user":user}

def shownotes(request):
    notesalldata=mynotes.objects.all()
    return render(request,'showNotes.html',{'allnotes':notesalldata})