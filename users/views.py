from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm

# index page
def index(request):
  return redirect('login')

# index page
@login_required
def home(request):
  return render(request, "users/home.html")

# users dashboard
@login_required
def dashboard(request):
  return render(request, "users/dashboard.html")

# register new user view
def register(request):
  if request.method == "GET":
    return render(
      request, "users/register.html",
      {"form": CustomUserCreationForm}
    )
  elif request.method == "POST":
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      # user = form.save()
      user = form.save(commit=False)
      user.backend = "django.contrib.auth.backends.ModelBackend"
      user.save()
      login(request, user)
      return redirect(reverse("dashboard"))
    return render(
      request, "users/register.html",
      {"form": CustomUserCreationForm}
    )
