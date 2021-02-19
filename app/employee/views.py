from django.shortcuts import render, redirect

from app.employee.forms import EmployeeForm


def createEmployee(request):
    template_name = 'create_employee.html'
    if request.method == 'GET':
        form = EmployeeForm()
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list_menus')

    return render(request, template_name, {'form': form})

