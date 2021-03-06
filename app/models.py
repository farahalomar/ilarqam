from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=254)
    abstract = models.TextField()
    image = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=None)
    date = models.DateField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=254)
    number_of_members = models.CharField(max_length=254)
    twitter_thread = models.URLField(max_length=200)
    project_email = models.EmailField(max_length=254)
    project_link = models.URLField(max_length=200)

    def __str__(self):
        return self.title


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    membership = models.CharField(verbose_name="(٢٠١٩-الآن)", max_length=100)
    picture = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=None)
    lates_projects = models.ManyToManyField(
        Project)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    twitter_account = models.URLField(max_length=200)
    ilarqam_email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name
