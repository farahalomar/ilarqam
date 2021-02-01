from django.contrib import admin
from .models import Project, Country, City, Person

admin.site.register(Project)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Person)
