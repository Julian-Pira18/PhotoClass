from . import views
from django.urls import path

urlpatterns = [
    path('photos/', views.show_editor, name="photos"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),   
    path('logout/', views.signout, name="signout"),
    path('',views.show_menu, name='home')
]