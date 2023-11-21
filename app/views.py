from django.shortcuts import render

# Create your views here.
def abc(request):
    a=10
    
    
    return render(request,'abc.html',a)