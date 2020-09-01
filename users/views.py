from django.shortcuts import render,redirect
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.decorators import  login_required
from  .form import  UserRegistration
# Create your views here.

def Registration(request):
    if request.method=='POST':
      form=UserRegistration(request.POST)
      form.save()
      return redirect('emp_insert')
    else:
        form = UserRegistration()

    return  render(request,'users/register.html',{'form':form})

@login_required
def Profile(request):
    return render(request,'users/profile.html')

