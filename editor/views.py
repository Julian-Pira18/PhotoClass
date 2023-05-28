from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .My_Stack import Stack, Node


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
def show_editor(request):
    return render(request, 'editor.html', {
        "imagen": dataList
    })

def show_menu(request):
    return render(request, 'index.html')