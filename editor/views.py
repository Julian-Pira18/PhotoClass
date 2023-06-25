from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .My_Stack import Stack, Node
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from .AVL import avl_photos, avl_search, Avl_to_list,avl_eliminados
import shutil
from .Hash_table import Hash_Table, object_hash,update_hash

dataStack = Stack()

updates = object_hash()
object_avl = avl_photos(updates)
eliminados = avl_eliminados()


# Create your views here.
def show_menu(request):
    return render(request, 'index.html')

def show_editor(request):
    avl_list = cargar_avl()
    return render(request, 'editor.html', {
        "imagen": avl_list
    })

def show_photo(request, indice):    
    # photo_list = avl_search(indice)  
    photo_list = avl_search(indice, object_avl)
    photo = photo_list.label
    if request.method == "GET":
        return render(request, 'clasificar.html',{
            "photo": photo
        })
    
    elif request.method == "POST":
        datos = []
        datos.append(request.POST["opt_schema"])
        datos.append(request.POST["opt_type"])
        datos.append(request.POST["opt_iso"])
        datos.append(request.POST["opt_tmp"])
        datos.append(request.POST["opt_diafragma"])
        Indice = request.POST["indice"]
        datos_final = []
        print(f"Indice:{indice}")
        for i in range(3):
            if i == 2:
                i = "Iso:"+ datos[i] + " Tiempo_obturacion" + datos[i+1] + " Diafragma" + datos[i+1]
                datos_final.append(i)
            else:
                datos_final.append(datos[i])

        obj = avl_search(indice, object_avl)
        name_obj = obj.label.data.replace("fotos_book/","")
        updates = load_updates()
        updates = update_hash(updates, name_obj, datos_final)
        return redirect("photos")

def load_updates():
    return updates


def deleted_photo(request, indice):
    carpeta_origen = "C:/Users/Julian/Documents/Estructuras_proyect/PhotoClass/editor/templates/static/imagenes/fotos_book/"
    carpeta_destino = "C:/Users/Julian/Documents/Estructuras_proyect/PhotoClass/editor/templates/static/imagenes/eliminados/"
    
    photo_to_delete = avl_search(indice, object_avl)
    path_photo = photo_to_delete.label.data
    path_photo = path_photo.replace("fotos_book/","")
    shutil.move(carpeta_origen + path_photo,carpeta_destino)

    avl_list = cargar_avl()
    return render(request, 'editor.html', {
        "imagen": avl_list
    })

def cargar_avl():
    object_avl = avl_photos(updates)
    avl_list = Avl_to_list(object_avl)
    return avl_list

def show_papelera(request):
    return render(request, 'papelera.html')

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
    eliminados = avl_eliminados()
    avl_lista = Avl_to_list(eliminados)
    return render(request, 'papelera.html',{
        "imagen": avl_lista
    }) 

def papelera_regain(request,indice):
    eliminados = avl_eliminados()
    carpeta_origen = "C:/Users/Julian/Documents/Estructuras_proyect/PhotoClass/editor/templates/static/imagenes/eliminados/"
    carpeta_destino = "C:/Users/Julian/Documents/Estructuras_proyect/PhotoClass/editor/templates/static/imagenes/fotos_book/"
    
    photo_to_delete = avl_search(indice, eliminados)
    path_photo = photo_to_delete.label.data
    print(path_photo)
    path_photo = path_photo.replace("fotos_book/","")
    shutil.move(carpeta_origen + path_photo,carpeta_destino)
    
    avl_lista = load_eliminated()
    return render(request, 'papelera.html',{
        "imagen": avl_lista
    })

def load_eliminated():
        eliminados = avl_eliminados()
        avl_lista = Avl_to_list(eliminados)
        return avl_lista