from . import views
from django.urls import path

urlpatterns = [
    path('photos/', views.show_editor, name="photos"),
    path('photos/clasificar/<int:indice>', views.show_photo, name="photo"),
    path('photos/<int:indice>', views.deleted_photo, name="photo_eliminada"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),   
    path('logout/', views.signout, name="signout"),
    path('clasificar/', views.clasificar, name="clasificar"),
    path('buscar/', views.buscar, name="buscar"),
    path('papelera/', views.papelera, name="papelera"),
    path('papelera/<int:indice>', views.papelera_regain, name="papelera_regain"),
    path('',views.show_menu, name='home')
]