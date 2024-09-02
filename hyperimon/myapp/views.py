from django.shortcuts import render, redirect
from .models import Project

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'myapp/project_list.html', {'projects': projects})

def project_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roof_length = request.POST.get('roof_length')
        roof_width = request.POST.get('roof_width')
        project = Project.objects.create(name=name, roof_length=roof_length, roof_width=roof_width)
        return redirect('project_list')
    return render(request, 'myapp/project_create.html')
