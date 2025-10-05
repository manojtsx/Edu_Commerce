from django.shortcuts import render
from .models import User
from .models import Admin
from django.db import IntegrityError, transaction
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
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
        try:
            with transaction.atomic():
                # ✅ Create user
                hashed_password = make_password(password)
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    phone=phone,
                    password=hashed_password,
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