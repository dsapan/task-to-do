from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from random import randrange
from task_to_doproject.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

# Create your views here.

def usignup(request):
	if request.method =="POST":
		un=request.POST.get('un')
		pw1=request.POST.get('pw1')
		pw2=request.POST.get('pw2')
		if pw1 == pw2:
			try:
				usr=User.objects.get(username=un)
				return render(request,'usignup.html',{'msg':'Username Already Registered '})
			except User.DoesNotExist:
				usr=User.objects.create_user(username=un,password=pw1)
				usr.save()
				print("hey sign")
				return redirect('ulogin')
		else:
			return render(request,'usignup.html',{'msg':'password did not match '})
	else:
		return render(request,'usignup.html')

def ulogin(request):
	if request.method=="POST":
		un=request.POST.get('un')
		print(un)
		pw=request.POST.get('pw')
		print(pw)
		usr=authenticate(username=un,password=pw)
		print("hey login")

		if usr is None:
			return render(request,'ulogin.html',{'msg':'Invalid Login'})

		else:
			login(request,usr)
			return redirect('home')

	else:
		return render(request,'ulogin.html')

def ulogout(request):
	logout(request)
	return redirect('ulogin')

def uforgotpass(request):
	if request.method == "POST":
		un = request.POST.get('un')
		em = request.POST.get('em')
		try:
			usr=User.objects.get(username=un) 
			pw=""
			text="1234567890abcdefghijkASDFGHJ"
			for i in range(6):
				pw=pw+text[randrange(len(text))]
			print(pw)
			subject="Welcome to Task To Do App"
			msg=" Your password for login is  "+str(pw)+"\n Please set new password after login"
			send_mail(subject,msg,EMAIL_HOST_USER,[em])
			usr=User.objects.get(username=un)
			usr.set_password(pw)
			usr.save()
			return redirect('ulogin')

		except User.DoesNotExist:
			return render(request,'uforgotpass.html',{'msg':'Username /Email-Id Does Not Exists '})
	else:
		return render(request,'uforgotpass.html')


def uchangepass(request):
	if request.method=="POST":
		un=request.POST.get('un')
		pw1=request.POST.get('pw1')
		pw2=request.POST.get('pw2')
		if pw1==pw2:
			usr=User.objects.get(username=un)
			usr.set_password(pw1)
			usr.save()
			return redirect('ulogin')
		else:
			return render(request,'uchangepass.html',{'msg':'Password does not match! '})
	else:
		return render(request,'uchangepass.html')

