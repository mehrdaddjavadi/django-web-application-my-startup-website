from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import EmailForMagazineForm
from .models import EmailForMagazine
from django.http import HttpResponseRedirect



# def registerEmailForMagazineForm(request):
#     if request.method == 'POST':
#         form = EmailForMagazineForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data.get('email')  
#             messages.success(request,f'عضویت شما در خبرنامه آسمانکشت با  {email} با موفقیت انجام شد.')
#             return(redirect('articles:post_list'))
#     else:
#         form = EmailForMagazineForm()
#     return render(request,'emailformagazine.html',{'form':form})


# def email_list_signup(request):
#     form =EmailForMagazineForm(request.POST or None)
#     if request.method =="POST":
#         if form.is_valid():
#             email_signup_qs=EmailForMagazine.objects.filter(email=form.instance.email)
#             if email_signup_qs.exists():
#                 message.info(request,"شما در حال حاضر در خبرنامه آسمانکشت عضو هستید")
#             else:
#                 subscribe(form.instance.email)
#                 form.save()
#                 message.success(request,"عضویت  شما در خبرنامه آسمان کشت با موفقیت انجام شد")
#     return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def email_list_signup(request):
    form =EmailForMagazineForm(request.POST or None)
    if request.method =="POST":
        if form.is_valid():
            email_signup_qs=EmailForMagazine.objects.filter(email=form.instance.email)
            if email_signup_qs.exists():
                messages.info(request ,"شما در حال حاضر در خبرنامه آسمانکشت عضو هستید")
            else:
                form.save()
                messages.success(request,"عضویت  شما در خبرنامه آسمان کشت با موفقیت انجام شد")
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    