from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render,redirect
from django.views import View

from .models import Project,Contactme

def home(request):
    project = Project.objects.all()
    context={
        'project':project
    }
    return render(request, 'home.html',context)


def projects(request):
    project = Project.objects.all()
    context = {
        'project': project
    }
    return render(request, 'projects.html',context)


def resume(request):
    project = Project.objects.all()
    context = {
        'project': project
    }
    return render(request, 'resume.html',context)


def aboutme(request):
    return render(request, 'aboutme.html')


class Contact(View):
    def get(self, request):
        return render(request, 'contactme.html')
    def post(self,request):
        postData = request.POST
        name = postData.get('name')
        email = postData.get('email')
        phone = postData.get('phonenumber')
        company =  postData.get('company')
        message = postData.get('query')
        form = Contactme(name=name,
                            email=email,
                            phone=phone,
                            company=company,
                            description=message)
        form.register()

        email = EmailMessage(
            'New Message Send From Portfolio',
            'Message from : '+name+
            'Email: '+email+
            'Phone : '+phone+
            'message: '+message+
            'company: '+company,
            settings.EMAIL_HOST_USER,
            ['venkateshvenky5408@gmail.com','gollaprolu.venkatesh1501@gmail.com'],
        )
        email.fail_silently = False
        email.send()
        return redirect('/?success=1')