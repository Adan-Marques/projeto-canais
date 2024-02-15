from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home_totver(request):
    return render(request,'home-totver.html')

@login_required
def dashboard(request):
    return render(request,'dashboard.html')
