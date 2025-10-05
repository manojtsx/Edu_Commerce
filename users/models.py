from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('teacher', 'Teacher'),
        ('learner', 'Learner'),
    )
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length = 255)
    role = models.CharField(max_length= 50, choices=ROLES)
    updated_at = models.DateTimeField(auto_now= True)
    def __str__(self):
        return self.username
    
class Admin(models.Model):
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username