from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def count(request):
    text=request.POST['text']
    countword=len(text.split())
    return render(request, 'count.html', {'countword' : countword})