from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.conf import settings

def home(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f"New Contact from {name}"
        full_message = f"Sender: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,
                ['tmunene75@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Thank you for reaching out! I will get back to you soon.')
        except BadHeaderError:
            messages.error(request, 'Invalid header found.')
        except Exception as e:
            messages.error(request, f'Something went wrong: {e}')

        return redirect('home')

    return redirect('home')
