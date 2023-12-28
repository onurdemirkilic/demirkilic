from django.db import models
from django.contrib.auth.models import User
from random import randint, choice
# Create your models here.


class TicketOnur (models.Model) : 
    name = models.CharField(max_length=120)
    order = models.CharField(max_length=30)
    email = models.TextField()
    kutu = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__ (self) : 
        if self.status == False : 
            read = "Okunmadi"
        else : 
            read = "Okundu"
        ticket_status = f"{self.name} {self.order} {read}"
        return ticket_status


class TicketIpek (models.Model) : 
    name = models.CharField(max_length=120)
    order = models.CharField(max_length=30)
    email = models.TextField()
    subject = models.TextField()
    message = models.TextField()
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__ (self) : 
        if self.status == False : 
            read = "Okunmadi"
        else : 
            read = "Okundu"
        ticket_status = f"{self.name} {self.order} {read}"
        return ticket_status


class ModelService (models.Model) : 
    name = models.CharField(max_length=30) 
    image = models.ImageField()
    image2 = models.ImageField()

    def __str__ (self) : 
        return self.name


class CustomerService (models.Model) : 
    name = models.CharField(max_length=66)
    content = models.TextField()
    img1 = models.ImageField(blank=True)
    img2 = models.ImageField(blank=True)
    img3 = models.ImageField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_number = randint(1,99999999)
    
    def __str__ (self) : 
        return_it = f"{self.name} {self.order_number}"
        return return_it


class IntelligenceService (models.Model) : 
    name = models.CharField(max_length=66)
    phone_number = models.CharField(max_length=9999)
    job = models.CharField(max_length=120)
    home_adress = models.CharField(max_length=9999)
    business_adress = models.CharField(max_length=9999)
    car_plate = models.CharField(max_length=35)
    content = models.TextField()
    intelligence_links = models.TextField()
    code_list = ["A","B","C","D","E","G"]
    speacial_code = f"{choice(code_list)}{randint(1,99999)}"
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    code = models.CharField(max_length=100,default=speacial_code)
    TOP_SECRET = models.BooleanField(default=False)
   

    def __str__ (self) : 
        if self.TOP_SECRET == False : 
            CHECK_TOP_SECRET = " "
        else : 
            CHECK_TOP_SECRET = "TOP SECRET"
        return_it = f"{self.name}  {self.code}  {CHECK_TOP_SECRET}"
        return return_it 

class ArchiveService (models.Model) : 
    name = models.CharField(max_length=66,)
    code_list = ["A","B","C","D","E","G"]
    speacial_code = f"{choice(code_list)}{randint(1,99999)}"
    code = models.CharField(max_length=100,default=speacial_code)
    file = models.FileField(blank=False)
    image = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)

    def __str__ (self) :
        return_it = f"{self.name} -> {self.code}" 
        return return_it
    