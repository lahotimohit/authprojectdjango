from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from . import forms
from django.contrib.auth.decorators import login_required

@csrf_exempt
def registerPage(request):
    form = forms.MyUserCreationForm()
    if request.method == "POST":
        form = forms.MyUserCreationForm(request.POST, request.FILES)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return redirect('home')
    return render(request, 'hospital/signup.html', {'form': form})


@login_required
def home(request):
    user = request.user
    return render(request,'hospital/index.html', {'user':user})