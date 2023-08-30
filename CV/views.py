from django.shortcuts import render
from CV.models import Certificates, Projects
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    certificates = Certificates.objects.all()
    projects = Projects.objects.all()
    shepel = User.objects.get(username='Shepel')
    return render(request, 'CV/index.html', {
        'projects': projects,
        'certificates': certificates,
        'user': shepel,
    })

