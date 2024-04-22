from django.db import models
from django.urls import reverse
# Create your models here.
class SnackInfo(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    image = models.ImageField(upload_to='photos/snack')
    from_to=models.CharField(max_length=100)
    phone=models.CharField(max_length=100,blank=True,null=True)
    email=models.CharField(max_length=100 ,blank=True,null=True)
    instagram_link=models.CharField(max_length=400 ,blank=True,null=True)
    facebook_link=models.CharField(max_length=400 ,blank=True,null=True)
    x_link=models.CharField(max_length=400 ,blank=True,null=True)
    def __str__(self):
        return self.name

class Events(models.Model):
    title=models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/event')
    description=models.TextField()
    def __str__(self):
        return self.title
class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100, unique=True)
    def get_url(self):
        return reverse('category', args=[self.slug])
    def __str__(self):
        return self.name
    
class Menu(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=80)
    description=models.TextField()
    image = models.ImageField(upload_to='photos/menu')
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField()
    is_availabele = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, unique=True)
    def availabillity(self):
        if self.stock <= 0:
            self.is_availabele = False
        else:
            self.is_availabele = True

    def save(self, *args, **kwargs):
        self.availabillity()
        super().save(*args, **kwargs)
    def get_url(self):
        reverse('food_details',args=[self.category.slug,self.slug])
    def __str__(self):
        return self.name