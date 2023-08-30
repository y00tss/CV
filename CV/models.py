from django.db import models

# Create your models here.

class Certificates(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    school_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='CV/images/certificates/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'


class Projects(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    technologies = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='CV/images/projects/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'