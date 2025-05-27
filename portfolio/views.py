from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # i.
        send_mail(
            f"New Contact from {name}",
            message,
            email,
            ['tmunene75@gmail.com'],  # your receiving email
        )

        messages.success(request, 'Thank you for reaching out! I will get back to you soon.')
        return redirect('home') 

    return redirect('home')  