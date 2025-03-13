from django.shortcuts import render

# Create your views here.
def my_first_view(request):
    return render(request, "base.html")

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')