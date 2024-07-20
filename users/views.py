from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}! Please log in')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('logout-done')

def logout_done(request):
    return render(request,'users/logout.html')