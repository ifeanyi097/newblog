from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model



def index(request):
    return render(request, 'app/index.html')


def superi(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        e = request.POST.get('email')
        p = request.POST.get('password')
        user = get_user_model().objects.create_superuser(username=u,email=e, password=p,)
        return redirect('index')
    return render(request, 'app/super.html')