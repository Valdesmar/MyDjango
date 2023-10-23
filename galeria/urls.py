from django.urls import path
from galeria.views import index, imagem
# git correction 123123123234

urlpatterns =[
    path('', index, name='index'),
    path('imagem/<int:photo_id>', imagem, name='imagem'),
] 
