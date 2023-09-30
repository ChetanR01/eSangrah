from django.db import models

# Create your models here.
class Offer(models.Model):
    image=models.ImageField(upload_to="offers_img")

class Fruit(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="fruits_img")
    desc = models.CharField(max_length=100)
    price = models.FloatField(max_length=6)
    def __str__(self):
        return self.name
    
class DryFruit(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="dryfruit_img")
    desc = models.CharField(max_length=100)
    price = models.FloatField(max_length=6)
    def __str__(self):
        return self.name    
    
class Vegetable(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="vegetable_img")
    desc = models.CharField(max_length=100)
    price = models.FloatField(max_length=6)
    def __str__(self):
        return self.name    

class DailyNeed(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="dailyneed_img")
    desc = models.CharField(max_length=100)
    price = models.FloatField(max_length=6)
    def __str__(self):
        return self.name        

class Electronic(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="electronic_img")
    desc = models.CharField(max_length=100)
    price = models.FloatField(max_length=6)
    def __str__(self):
        return self.name   

class Stationary(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="stationary_img")
    desc = models.CharField(max_length=20)
    price = models.FloatField(max_length=6)
    def __str__(self):
        return self.name      

class Xerox(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    desc = models.TextField()
    file = models.FileField(upload_to="document")
    date = models.DateTimeField()
    def __str__(self):
        return self.name      

class Product(models.Model):
    name = models.CharField(max_length=10)
    image = models.ImageField(upload_to="products_img")
    desc = models.CharField(max_length=20)
    longdesc = models.CharField(max_length=300)
    price = models.FloatField(max_length=6)
    # product_id = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    desc = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return f"Message form {self.name} on {self.date}"
    