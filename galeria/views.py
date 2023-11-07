from django.shortcuts import render, get_object_or_404, redirect

from galeria.models import Photo

from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado!')
        return redirect('login')
    
    photos = Photo.objects.order_by("data_photo").filter(publicada=True)
    return render(request, "galeria/index.html", {"cards": photos})

def imagem(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    return render(request, "galeria/imagem.html", {"photo": photo})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado!')
        return redirect('login')

    photos = Photo.objects.order_by("data_photo").filter(publicada=True)

    if "buscar" in request.GET['buscar']:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            photos = photos.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/buscar.html", {"cards": photos})
