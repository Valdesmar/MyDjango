from django.shortcuts import render, get_object_or_404
from galeria.models import Photo
# Test adas12321321123234


def index(request):
    photos = Photo.objects.order_by("data_photo").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": photos})

def imagem(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    return render(request, 'galeria/imagem.html', {"photo": photo})
