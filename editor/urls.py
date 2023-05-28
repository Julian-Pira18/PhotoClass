from . import views
from django.urls import path

urlpatterns = [
    path('photos/', views.show_editor, name="photos")
]