from .models import Core

def core(request):

    if Core.objects.all():
        core = Core.objects.get(id=1)
    else:
        core = ''

    return {
        'core': core
    }