from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def landing_page(request):
    return render(request, 'landing/landing.html')

def recruiter_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        #user = authenticate(request, username=email, password=password)

        # if user is not None:
            # login(request, user)
            # messages.success(request, "Login successful!")
            # Redirect to Chainlit after successful login
        return redirect('chainlit_redirect')  # URL name for Chainlit redirection
        # else:
        #     messages.error(request, "Invalid email or password.")
    
    return render(request, 'login/login.html')

def chainlit_redirect(request):
    # Redirect to Chainlit running on port 9000
    return redirect('http://127.0.0.1:8000/{email}')
