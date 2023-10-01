from django.conf import settings
from django.shortcuts import redirect, render

from .forms import ProfileForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.mail import EmailMessage, get_connection
from django.contrib.sites.shortcuts import  get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import generate_token
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        
        # Some Validations
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!!")
            return HttpResponseRedirect(request.path_info)
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use!!")
            return HttpResponseRedirect(request.path_info)
        
        if len(password1) < 8 or len(password1) > 16:                
            messages.error(request,"Password length must be 8-16!!")
            return HttpResponseRedirect(request.path_info)
        
        if password1 != password2:
            messages.error(request,"Password didn't match!!")
            return HttpResponseRedirect(request.path_info)
        
            
        
        # Validation successful
        new_user = User.objects.create_user(username=username, email=email, password=password2)
        new_user.save()
        
        # profile = Profile(new_user = new_user)
        profile = Profile()
        profile.user = new_user 
        profile.save()
        
        
        with get_connection(  
            host=settings.EMAIL_HOST, 
            port=settings.EMAIL_PORT,  
            username=settings.EMAIL_HOST_USER, 
            password=settings.EMAIL_HOST_PASSWORD, 
            use_tls=settings.EMAIL_USE_TLS  
        ) as connection:  
            subject = "Confirmation email"
            email_from = settings.EMAIL_HOST_USER  
            recipient_list = [new_user.email]  
            current_site = get_current_site(request)   # getting the current site domain whether localhost or smth like .com, .org
            
            message = render_to_string("user_accounts/confirmation_email.html", {
            'name': new_user.get_username(),
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),  #generating the unique id using pk which uniquely identifies the token for particular user
            'token': generate_token.make_token(new_user)
            })
            mail = EmailMessage(subject, message, email_from, recipient_list, connection=connection)  
            mail.send(fail_silently=True)
           
           # acc created success msg then go to login page
        new_acc = True
        messages.success(request, "Your account has been created successfully!!")
        return render(request, 'user_accounts/login.html', context={'new_acc':new_acc})
        
    return render(request, 'user_accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        
        user = authenticate(username = username, password = password)
        
        if user is not None:
            auth_login(request, user)             
            return redirect("home")
        else:
            messages.error(request, "Sorry, credentials not found!!")
            return redirect("login")
    
    return render(request, 'user_accounts/login.html')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (ValueError,TypeError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and generate_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Your account has been verified successfully!!")
        return redirect("login")

def logout(request):
    auth_logout(request)
    return redirect("login")


def update_profile(request):
    if request.method == "POST":
        print("hello")
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            
            my_details = form.instance  
            
            messages.success(request,"Profile saved successfully!!")
            return render(request, "user_accounts/my_profile.html", context={'my_details':my_details})
        else:
            messages.error(request, "Invalid information!!")
            return render(request, "user_accounts/update_profile.html", context={'form':form})
    
    try:
        my_details = Profile.objects.get(user=request.user)
        if my_details:
            return render(request, "user_accounts/my_profile.html", context={'my_details':my_details})
    except:
        form = ProfileForm(None)
        return render(request, "user_accounts/update_profile.html", context={'form':form})
   
def update_existing_profile(request):
    try:
        my_details = Profile.objects.get(user=request.user)
        if my_details:
            my_details.delete()
            return redirect("update_profile")            
    except:
        print("Could not update profile")
        pass
  
