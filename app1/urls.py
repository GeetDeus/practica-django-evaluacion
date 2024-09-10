from django.urls import path
from . import views  # Importa las vistas de app1

urlpatterns = [
    path('vista1/', views.vista1, name='vista1'),
    path('vista2/', views.vista2, name='vista2'),
]
