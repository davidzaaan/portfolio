from django.shortcuts import render, redirect
from django.core.mail import send_mail

def index(request):

    if request.method == 'POST':
        guest_name = request.POST.get('name')
        guest_email = request.POST.get('email')
        guest_feedback = request.POST.get('comments')

        send_mail(
            f'{guest_name} saw your portfolio',
            f'{guest_feedback} by: {guest_email}',
            guest_email,
            ["odmh2711@gmail.com"],
            fail_silently=True,
        )

        return redirect('thank_you')

    return render(request, 'index.html', {})


def thank_you(request):
    return render(request, 'ty.html', {})