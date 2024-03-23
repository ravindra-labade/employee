from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def add_employee(request):
    template_name = 'emp/add.html'
    form = EmployeeForm()
    if request.method  == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {"form": form}
    return render(request, template_name, context)

def show_employee(request):
    template_name = 'emp/show.html'
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, template_name, context)


def update_employee(request, pk):
    obj = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=obj)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'emp/add.html'
    context = {"form": form}
    return render(request, template_name, context)


def delete_employee(request, pk):
    obj = Employee.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, 'emp/confirm.html')
