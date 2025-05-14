
from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    SPECIES_CHOICES = (
        ('dog', 'Dog'),
        ('cat', 'Cat'),
    )
    
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets')
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=20, choices=SPECIES_CHOICES)
    breed = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='unknown')
    age = models.PositiveIntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)  # in kg
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='pet_profiles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.get_species_display()} owned by {self.owner.username})"

