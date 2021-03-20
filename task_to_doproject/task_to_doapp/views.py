from django.shortcuts import render,redirect
from .forms import TForm
from .models import TModel

# Create your views here.

def home(request):
	if request.user.is_authenticated:
		return render(request,'home.html')
	else:
		return redirect('ulogin')

def createtask(request):
	if request.method=="POST":
		f=TForm(request.POST)
		if f.is_valid():
			f.save()
			fm=TForm()
			return render(request,'createtask.html',{'fm':fm,'msg':'Task Uploaded'})
		else:
			fm=TForm()
			return render(request,'createtask.html',{'fm':f,'msg':'Error'})
	else:
		fm=TForm()
		return render(request,'createtask.html',{'fm':fm})


def viewtask(request):
	data=TModel.objects.all()
	return render(request,'viewtask.html',{'data':data})
