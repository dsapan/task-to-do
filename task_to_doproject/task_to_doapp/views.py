from django.shortcuts import render,redirect
from .forms import TForm
from .models import TModel
import requests
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
	if request.user.is_authenticated:
		try:
			a1="https://newsapi.org/v2/top-headlines"
			a2="?sources=" +"the-hindu"
			a3="&apiKey=" + "dcf42dec7d614e778d3dcd8616ab8182"
			wa= a1+a2+a3
			res= requests.get(wa)
			#print(res)
			data= res.json()
			#print(data)

			info=data['articles']
			return render(request,'home.html',{'info':info})
		except Exception as e:
			return render(request,'home.html',{'err':'Issue'})
	else:
		return redirect('ulogin')

@login_required(login_url='http://127.0.0.1:8000/ulogin/')
def createtask(request):
	if request.method=="POST":
		f=TForm(request.POST)
		if f.is_valid():
			tno=f.cleaned_data["tno"]
			task=f.cleaned_data["task"]
			t=TModel(tno=tno,task=task,task_dt=request.POST.get('task_dt'),user=request.user)
			t.save()
			fm=TForm()
			return render(request,'createtask.html',{'fm':fm,'msg':'Task Uploaded'})
		else:
			fm=TForm()
			return render(request,'createtask.html',{'fm':f,'msg':'Error'})
	else:
		fm=TForm()
		return render(request,'createtask.html',{'fm':fm})

@login_required(login_url='http://127.0.0.1:8000/ulogin/')
def viewtask(request):
	log_user=request.user
	data=TModel.objects.filter(user=log_user)
	return render(request,'viewtask.html',{'data':data})

@login_required(login_url='http://127.0.0.1:8000/ulogin/')
def checkweather(request):
	if request.method == "POST":
		try:
			city=request.POST.get('city')
			a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
			a2="&q=" + city
			a3="&appid=" + "c6e315d09197cec231495138183954bd"
			wa=a1+ a2+ a3

			res=requests.get(wa)
			#print(res)

			data=res.json()
			#print(data)

			temp=data['main']['temp']
			print("temperature = " ,temp)

			desc=data['weather'][0]['description']
			print('description= ', desc)
			icon="http://api.openweathermap.org/img/w/"+data['weather'][0]['icon']+ ".png"
			msg="Temp= "+str(temp) + "Descrip= " +str(desc)
			return render(request,'checkweather.html',{'msg':msg,'icon':icon})

		except Exception as e:
			return render(request,'checkweather.html',{'msg':'City Not Found '})
	else:
		return render(request,'checkweather.html')

@login_required(login_url='http://127.0.0.1:8000/ulogin/')		
def deletetask(request,id):
	tdata=TModel.objects.get(task=id)
	tdata.delete()
	return redirect('viewtask')





