from django.shortcuts import render
from .models import User
from .models import Admin
from django.db import IntegrityError, transaction
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.hashers import make_password

User = get_user_model()

# Create your views here.
def register(request):
    if request.method == 'POST':
        # Handle form submission logic here
        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        if not username or not email or not first_name or not last_name or not password or not password_confirm:
            messages.error(request, "All fields are required.")
            return  render(request, 'admin-register.html')
        if password != password_confirm:
            messages.error(request, "Passwords do not match.")
            return  render(request, 'admin-register.html')
        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return  render(request, 'admin-register.html')
        if "@" not in email or "." not in email:
            messages.error(request, "Invalid email address.")
            return  render(request, 'admin-register.html')
        if len(phone) < 10 or not phone.isdigit():
            messages.error(request, "Invalid phone number.")
            return  render(request, 'admin-register.html')
        isUserNameTaken = User.objects.filter(username=username).exists()
        if isUserNameTaken:
            messages.error(request, "Username is already taken.")
            return render(request, "admin-register.html")
        isEmailTaken = User.objects.filter(email=email).exists()
        if isEmailTaken:
            messages.error(request, "Email is already taken.")
            return render(request, "admin-register.html")
        try:
            with transaction.atomic():
                # ✅ Create user
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    phone=phone,
                    password=password,
                    role="admin"
                )

                # ✅ Create corresponding admin record
                admin = Admin.objects.create(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    user=user
                )

            messages.success(request, "Admin account created successfully!")
            return redirect("login")

        except IntegrityError:
            messages.error(request, "Database error occurred. Please try again.")
            return render(request, "admin-register.html")

        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return render(request, "admin-register.html")
    return render(request, 'admin-register.html')

def login_view(request):
    print(request.user, 'request')
    if request.user.is_authenticated:
        return redirect("/adminpanel/dashboard")
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password, "admin login")
        if not username or not password:
            messages.error(request, "All fields are required.")
            return  render(request, 'admin-login.html')
        try:
            user = User.objects.get(username=username)
            print(user, 'user')
            if user and user.check_password(password):
                print(user.role, 'role')
                if user.role != 'admin':
                    messages.error(request, "You are not authorized to access the admin panel.")
                    return render(request, 'admin-login.html')
                authenticatedUser = authenticate(request, username=username, password=password)
                if authenticatedUser is not None:
                    login(request, authenticatedUser)
                    messages.success(request, "Login successful!")
                    return redirect('/adminpanel/dashboard/')  # Redirect to Django admin dashboard
            else:
                messages.error(request, "Invalid username or password.")
                return render(request, 'admin-login.html')
        except User.DoesNotExist:
            messages.error(request, "Invalid username or password.")
            return render(request, 'admin-login.html')
    return render(request, 'admin-login.html')

def logout_view(request):
    logout(request)
    return redirect('/login')