from django.shortcuts import render

# Create your views here.
def datarender(request):
    output='this is a jjinga printing tag'
    d={'key':output}
    return render(request,'page1.html',context=d)