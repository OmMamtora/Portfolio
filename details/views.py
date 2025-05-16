from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
import os

from django.contrib.staticfiles.storage import staticfiles_storage

def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def projects(request):
    projects_show = [
        {
            "title":"To Do",
            "path":"images/Project_Images/To_do_home.png",
            "github_link":"https://github.com/OmMamtora/Projects/tree/main/todo"
        },
        {
            "title":"Music Player",
            "path":"images/Project_Images/Music_home.png",
            "github_link":"https://github.com/OmMamtora/Projects/tree/main/MusicPlayer"
        },
        {
            "title":"Recipe",
            "path":"images/Project_Images/recipe_add.png",
            "github_link":"https://github.com/OmMamtora/Projects/tree/main/recipe"
        },
        {
            "title":"Hospital Management System",
            "path":"images/Project_Images/HMS_AboutUs.PNG",
            "github_link":"https://github.com/OmMamtora/Projects/tree/main/Hospital%20Management%20System"
        },
        {
            "title":"Indus Exam And Lab Management",
            "path":"images/Project_Images/Indus_Exam And_Lab.png",
            "github_link":"https://github.com/OmMamtora/Projects/tree/main/Indus%20Lab%20and%20Exam%20Management"
        },
    ]
    return render(request,"projects.html",{"projects_show" : projects_show})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneNo = request.POST.get('phoneNo')
        message = request.POST.get('message')

        email_subject = "New Message from contact Form"
        email_message = f"Message from {name}\n\n Email-ID: {email}\n\n PhoneNo:{phoneNo}\n\n message:{message}"

        send_mail(
            email_subject,email_message,
            settings.DEFAULT_FROM_EMAIL,
            ['ommamtora9@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, "Thank you for reaching out! I'll get back to you soon.")

    return render(request, 'contact.html')

def resume(request):
    # Path to the resume file inside the static folder
    resume_path = os.path.join(settings.BASE_DIR, 'static', 'myResume', 'Resume(Om).pdf')
    
    if os.path.exists(resume_path):
        with open(resume_path, "rb") as resume_file:
            response = HttpResponse(resume_file.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'attachment; filename="Resume(Om).pdf"'
            return response
    else:
        return HttpResponse("Resume Not Found..", status=404)
