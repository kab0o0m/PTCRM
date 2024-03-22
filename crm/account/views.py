# views.py

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to dashboard or another page
                return redirect('/tutors')
    else:
        form = LoginForm()
    return render(request, 'account/account.html', {'form': form})


def logout_view(request):
    logout(request)
    # Redirect to a specific page after logout (e.g., home page)
    return redirect('/')
