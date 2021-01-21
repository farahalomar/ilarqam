from django.shortcuts import render
from .models import Project


def project_list(request):
    context = {
        "projects": Project.objects.all(),
    }
    return render(request, 'projectlist.html', context)
