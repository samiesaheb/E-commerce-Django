# core/views/contact.py

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render


def contact_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        full_message = f"From: {name} <{email}>\n\n{message}"

        try:
            send_mail(
                subject="New Contact Form Submission - Sky High",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["samie@skyhigh.co.th"],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully.")
            return redirect("contact")
        except Exception as e:
            messages.error(request, f"Error sending message: {e}")

    return render(request, "core/contact.html")
