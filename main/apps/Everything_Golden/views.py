from django.shortcuts import render, HttpResponse
#CONTROLLER
# Create your views here.
def index(request):
    return render(request, 'Everything_Golden/index.html')
