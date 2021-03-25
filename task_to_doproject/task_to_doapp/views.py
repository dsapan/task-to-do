from django.shortcuts import render,redirect
from .forms import TForm
from .models import TModel
import requests

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
		
def deletetask(request,id):
	tdata=TModel.objects.get(tno=id)
	tdata.delete()
	return redirect('viewtask')





