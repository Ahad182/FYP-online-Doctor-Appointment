from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.


class GenderModel(models.Model):
    gender = models.CharField(max_length=50)
    
    def __str__(self):
        return self.gender


class BloodModel(models.Model):
    blood = models.CharField(max_length=50)

    def __str__(self):
        return self.blood


class User(AbstractUser):

    
    m_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255 , unique=True)
    gender =models.CharField( max_length=100,null=True, blank=True)
    phone = models.CharField(max_length=255)
    address = models.TextField(max_length=300)
    image = models.ImageField(upload_to='profile/',blank=True , null=True)
    blood = models.CharField( max_length=100,null=True, blank=True)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.username
    
    
class Doctor(models.Model):

    Deparment_choices = [

        ('Orthopaedics','Orthopaedics'),
        ('Gynaecology & Obstetrics','Gynaecology & Obstetrics'),
        ('Chest & Vascular','Chest & Vascular'),
        ('Paediatrics & Neonatology','Paediatrics & Neonatology'),
        ('Psychiatry','Psychiatry'),
        ('Accident & Emergency','Accident & Emergency'),
        ('Dental Surgery','Dental Surgery'),
        
    
    ]


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctor-img/')
    deparment = models.CharField(max_length=255,choices=Deparment_choices )
    facebook = models.URLField(max_length=255)
    youtube = models.URLField(max_length=255)
    instagram = models.URLField(max_length=255)
    linkedin = models.URLField(max_length=255)
    twitter = models.URLField(max_length=255)

    def __str__(self):
        return self.user.first_name + " " + self.user.m_name 

class Appointment(models.Model):
    TIME_CHOICES=(
        ('3    PM', ' 3    PM'),
        ('3:30 PM', ' 3:30 PM'),
        ('4    PM', ' 4    PM'),
        ('4:30 PM', ' 4:30 PM'),
        ('5    PM', ' 5    PM'),
        ('5:30 PM', ' 5:30 PM'),
        ('6    PM', ' 6    PM'),
        ('6:30 PM', ' 6:30 PM'),
        ('7    PM', ' 7    PM'),
    )
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE, null=True,blank=True)
    patient = models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True)
    date = models.DateField(auto_now_add=True)
    time = models.CharField(max_length=100 , choices=TIME_CHOICES)
    hb= models.FloatField(max_length=100)
    bs= models.FloatField(max_length=100)
    bmi= models.FloatField(max_length=100)

    def __str__(self):
        return self.patient.username


