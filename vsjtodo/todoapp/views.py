from django.shortcuts import HttpResponse,render


# Create your views here.
def index(request):
    return render(request,"test.html")

    #return HttpResponse("Todo apps")

