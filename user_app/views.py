from django.shortcuts import render
from django.db import transaction
from django.contrib import messages
from django.shortcuts import redirect
from .models import Staff
from users.models import User

# Create your views here.
def add_staff(request):
    if(request.user.role != 'admin'):
        return render(request, 'unauthorized.html')
    if request.method == 'POST':
        # Handle form submission logic here
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if username is None or email is None or password is None or first_name is None or last_name is None:
            messages.error(request, 'Please fill all required fields!')
            return redirect('/adminpanel/add/staff')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('/adminpanel/add/staff')
    
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            return redirect('/adminpanel/add/staff')
        
        if email and "@" not in email:
            messages.error(request, 'Enter a valid email address!')
            return redirect('/adminpanel/add/staff')
        
        if phone and (not phone.isdigit() or len(phone) < 10):
            messages.error(request, 'Enter a valid phone number!')
            return redirect('/adminpanel/add/staff')
        
        # use transaction to ensure atomicity
        with transaction.atomic():
            user = User.objects.create_user(
                username=username,
                email=email,
                phone=phone,
                password=password,
                role='staff'
            )
            Staff.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                user=user,
                createdBy=request.user,  # Assuming the current logged-in user is creating the staff
                updatedBy=request.user
            )
        messages.success(request, 'Staff member added successfully!')
        return redirect('/adminpanel/add/staff')  # Redirect to a staff list page or any other page
        
    return render(request, 'add_staff.html')

def view_user_list(request):
    if(request.user.role != 'admin'):
        return render(request, 'unauthorized.html')
    users = User.objects.all().exclude(role='admin').order_by('-createdAt')
    return render(request, 'user_list.html', {'users': users})