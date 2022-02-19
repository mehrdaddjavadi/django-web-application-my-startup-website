from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

# Create your views here.
def contactus_view(request):
    if request.method == "POST":
        contact = Contact()
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.first_name=first_name
        contact.last_name=last_name
        contact.email=email
        contact.subject=subject
        contact.save()
        messages.success(request,"پیام شما ثبت شد؛ با تشکر و آرزوی پیروزی")
        return redirect("articles:post_list")

    return render(request,'contactus/contactus.html')