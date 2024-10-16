from django.shortcuts import render
from . models import Pets
from .forms import PestForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
def home(request):
    pests = Pets.objects.all().order_by('-uploaded_at')
    return render(request, 'petsystem/home.html', {'pests': pests})

def about(request):
    return render(request, 'petsystem/about.html')
def contact(request):
    return render(request, 'petsystem/contact.html')
@login_required
def connect(request):
    pets = Pets.objects.all().order_by('-uploaded_at')
    return render(request, 'petsystem/connect.html', {'pets': pets})
@login_required
def upload_pest(request):
    if request.method == 'POST':
        form = PestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to homepage after successful upload
    else:
        form = PestForm()
    return render(request, 'upload.html', {'form': form})

