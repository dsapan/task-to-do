from django.shortcuts import render,redirect
from .forms import TForm

# Create your views here.

def home(request):
	if request.user.is_authenticated:
		return render(request,'home.html')
	else:
		return redirect('ulogin')
def createtask(request):
	fm=TForm()
	return render(request,'createtask.html',{'fm':fm})