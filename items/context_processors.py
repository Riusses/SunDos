from items.models import Categoria

def categories(request):
    return {'categories':Categoria.objects.all()}