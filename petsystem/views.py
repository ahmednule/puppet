from django.shortcuts import render

def home(request):
    return render(request, 'petsystem/home.html')
def about(request):
    return render(request, 'petsystem/about.html')
def contact(request):
    return render(request, 'petsystem/contact.html')
def connect(request):
    return render(request, 'petsystem/connect.html')
