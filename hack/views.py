from django.shortcuts import render, redirect ,redirect,get_object_or_404
from .models import problem
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import problem_form
from .forms import contactus_form
from .models import contactus
from .models import Reg
from .forms import RegForm

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        forms = Reg.objects.filter(user = request.user)
        return render(request,'index.html',{'forms': forms})
    else:
        return render(request,'index.html')


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'password not matching..')
            return redirect('register')
        return redirect('team_register')

    else:
        return render(request,'register.html')


def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("index")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')




def form(request):
    if request.method == 'GET':
        problems = problem.objects.all()
        forms = Reg.objects.filter(user = request.user)
        context = {'form': problem_form() ,'problems':problems,'forms': forms}
        return render(request,"problems.html",context)
    else:
        form = problem_form(request.POST , request.FILES)
        newform = form.save(commit = False)
        newform.user = request.user
        newform.save()
        return redirect('index')

def contactus(request):
    if request.method == 'GET':
        return render(request,"contactus.html",{'form': contactus_form()})
    else:
        form = contactus_form(request.POST , request.FILES)
        newform = form.save(commit = False)
        newform.user = request.user
        newform.save()
        return redirect('index')


def team_register(request):

    if request.method == 'GET':
        return render(request,"team_register.html",{'form':RegForm()})
    else:
        form = RegForm(request.POST , request.FILES)
        newform = form.save(commit = False)
        newform.user = request.user
        newform.save()
        return redirect('index')


def editprofile(request,reg_pk):
    f1 = get_object_or_404(Reg,pk=reg_pk)
    if request.method == "GET":
        form = RegForm(instance=f1)
        return render(request,'edit.html',{'f1':f1,'form':form})
    else:
        form = RegForm(request.POST , request.FILES , instance = f1)
        form.save()
        return redirect('profile')


def profile(request):
    forms = Reg.objects.filter(user = request.user)
    return render(request , "profile.html",{'forms': forms})
