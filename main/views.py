from django.shortcuts import render, redirect
from django.http import Http404
from django.conf import settings
from django.core.mail import send_mail
from .models import TeamMember, Faculty, Club
import os


def index(request):
    return render(request, 'index.html')
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")


def flatpage(request, page):
    """Render a template file from `main/templates/` if it exists.

    This allows requests like `/about.html` to render `main/templates/about.html`.
    The function prevents directory traversal and only serves files that exist
    inside the `main/templates` directory.
    """
    # basic safety checks
    if ".." in page or page.startswith("/"):
        raise Http404()

    templates_dir = os.path.join(settings.BASE_DIR, 'main', 'templates')
    template_path = os.path.join(templates_dir, page)

    if not os.path.exists(template_path):
        raise Http404()

    # Pass team members, faculty members, and clubs to all templates
    context = {
        'team_members': TeamMember.objects.all(),
        'faculty_members': Faculty.objects.all(),
        'clubs': Club.objects.all()
    }
    
    return render(request, page, context)



def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        full_message = (
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Phone: {phone}\n\n"
            f"Message:\n{message}"
        )

        send_mail(
            subject=subject or "New contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=["contactmsg.ai@gmail.com"],  # change this
        )


        return redirect("index")  # or a “thank you” page

    return render(request, "index.html")