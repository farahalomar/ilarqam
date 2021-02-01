from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Project, Person


def project_list(request):
    context = {
        "projects": Project.objects.all(),
    }
    return render(request, 'projectlist.html', context)


def person_list(request):
    context = {
        "persons": Person.objects.all(),
    }
    return render(request, 'personlist.html', context)
