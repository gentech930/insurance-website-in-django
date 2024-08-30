from django.shortcuts import render
# from multiprocessing import context
from django.shortcuts import redirect
from django.contrib import messages
from .forms import EmployeeForm
from tkinter import Widget
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home or any other page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



from .models import Employee
def index(request):
      return render(request, "index.html")
def About(request):
      return render(request, "about.html")
def services(request):
     return render(request, "services.html")

def blog(request):
    return render(request, 'blog.html')

def Contact(request):
    form = EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        form.save()
        messages.success(request, 'Your message has been submitted!')
        form=EmployeeForm()
        return redirect('Contact')  # Redirect to the same page to see the updated data
    else:
        form = EmployeeForm()
    
    data=Employee.objects.all()

    context = {
        'form': form,
        'data' : data,
    }
    return render(request, 'contact.html', context)



   
   


# Create your views here.
