from django.db import models
from django.contrib import admin

# Create your models here.
class Staff(models.Model):
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    createdBy = models.ForeignKey(
        'users.User',
        related_name='staff_created_by',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    updatedBy = models.ForeignKey(
        'users.User',
        related_name='staff_updated_by',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username
    
class Teacher(models.Model):
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    updatedBy = models.ForeignKey(
        'users.User',
        related_name='teacher_updated_by',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username
    
class Learner(models.Model):
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    updatedBy = models.ForeignKey(
        'users.User',
        related_name='learner_updated_by',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username
    
admin.site.register(Staff)
admin.site.register(Teacher)
admin.site.register(Learner)