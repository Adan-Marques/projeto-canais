from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home_totver(request):
    return render(request,'usuarios/totvers/home-totver.html')

@login_required
def dashboard(request):
    return render(request,'usuarios/totvers/dashboard.html')
