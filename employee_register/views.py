from django.shortcuts import render,redirect
from .employeeform import  EmployeeForm
from django.contrib import  messages
from .models import Employee

# Create your views here.
def employee_list(request):
    employelist=Employee.objects.all()
    context={'emplist':employelist}
    return render(request,'employee_register/employee_list.html',context)

def employee_form(request, id=0):
    if request.method == "GET":
       if id==0:

         form=EmployeeForm()
         return render(request, "employee_register/employee_form.html",{'form':form} )
       else:
           employee=Employee.objects.get(pk=id)# filter with id
           form=EmployeeForm(instance=employee)
           return render(request, "employee_register/employee_form.html", {'form': form})


    else:#handling request post
        if id==0:
          form = EmployeeForm(request.POST)
        else:
            employee=Employee.objects.get(pk=id)
            form=EmployeeForm(request.POST, instance=employee)
        if form.is_valid():

            form.save()
            fullname=form.cleaned_data.get("fullname")
            messages.success(request, f' you  have been register  {fullname}! .')
            return redirect("/list")



def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect("/list")






