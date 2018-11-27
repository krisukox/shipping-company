from django.http import HttpResponse



def index(request):
    return HttpResponse("<h1>Here will be all vehicles</h1>")