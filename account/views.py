from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username=form.cleaned_data.get('username')  
#             messages.success(request,f'خوشامدید  {username}  پنل کاربری شما ایجاد شد')
#             return(redirect('articles:post_list'))
#     else:
#         form = RegistrationForm()
#     return render(request,'account/register.html',{'form':form})



def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
         messages.success(request,f"شما با نام کاربری{user.username} وایمیل{user.email} عضو سامانه هستید.")

    context = {}

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save() 
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = get_redirect_if_exists(request)
            if destination:
                return(redirect('articles:post_list'))
  


        else:
            context['registration_form'] = form

    return render(request,'account/register.html',context)


def logout_view(request):
    logout(request)
    return redirect("articles:post_list")

def login_view(request, *args, **kwargs):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("articles:post_list")

    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                destination = get_redirect_if_exists(request)
                if destination:
                    return redirect(destination)
                return redirect("articles:post_list")
        else:
            context['login_form']= form

    return render(request,"account/login.html", context)


def get_redirect_if_exists(request):
	redirect = None
	if request.GET:
		if request.GET.get("next"):
			redirect = str(request.GET.get("next"))
	return redirect
          
    
     