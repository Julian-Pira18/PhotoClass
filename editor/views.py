from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .My_Stack import Stack, Node
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError


dataStack = Stack()
dataStack.push("https://i.pinimg.com/originals/6d/ed/f7/6dedf72a2acdca56102ce23779df656e.jpg")
dataStack.push("https://i.pinimg.com/736x/1a/46/11/1a4611b27348f6eecaab0620710d1a83.jpg")
dataStack.push("https://i.pinimg.com/originals/14/55/00/1455005e7c2949c42f35c499631ffcec.jpg")
dataStack.push("https://i.pinimg.com/originals/14/55/00/1455005e7c2949c42f35c499631ffcec.jpg")
dataStack.push("https://i.pinimg.com/originals/14/55/00/1455005e7c2949c42f35c499631ffcec.jpg")
dataStack.push("https://i.pinimg.com/originals/14/55/00/1455005e7c2949c42f35c499631ffcec.jpg")
dataStack.push("https://i.pinimg.com/originals/14/55/00/1455005e7c2949c42f35c499631ffcec.jpg")
dataStack.push("https://i.pinimg.com/originals/14/55/00/1455005e7c2949c42f35c499631ffcec.jpg")
dataStack.push("https://i.pinimg.com/originals/14/55/00/1455005e7c2949c42f35c499631ffcec.jpg")
dataStack.push("https://i.pinimg.com/originals/14/55/00/1455005e7c2949c42f35c499631ffcec.jpg")
dataStack.push("https://i.pinimg.com/originals/14/55/00/1455005e7c2949c42f35c499631ffcec.jpg")
dataStack.push("https://i.pinimg.com/originals/14/55/00/1455005e7c2949c42f35c499631ffcec.jpg")

dataList = dataStack.show()

# Create your views here.

def show_menu(request):
    return render(request, 'index.html')

def show_editor(request):
    return render(request, 'editor.html', {
        "imagen": dataList
    })


def signup(request):
        if request.method == 'GET':
            return render(request, 'signup.html', {
                'form': UserCreationForm
            })
        else:
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.create_user(
                        username=request.POST['username'], password=request.POST['password1'])
                    user.save()
                    login(request, user)
                    return redirect('home')
                except IntegrityError:
                    return render(request, 'signup.html', {
                        'form': UserCreationForm,
                        'error': 'Username already exists'
                        })
                    
                
            return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'Password do not match'
            })
        
def signout(request):
    logout(request)
    return redirect('home') 


def signin(request):
    if request.method == 'GET':    
        return render(request, 'signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST ['password'])
        if user is None:    
            return render(request, 'signin.html',{
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'                
            })
        else:
            login(request, user)
            return redirect('home')


def clasificar(request):
    return render(request, 'clasificar.html') 

def buscar(request):
    return render(request, 'buscar.html') 

def papelera(request):
    return render(request, 'papelera.html') 