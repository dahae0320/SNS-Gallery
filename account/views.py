from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(request=request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(request=request, username=username, password=password)
      if user is not None:
        login(request, user)
      return redirect('index')
  else:
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def logout_view(request):
  logout(request)
  return redirect('index')

def signup_view(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
    return redirect('index')
  else:
    form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})