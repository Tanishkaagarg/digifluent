from django.db import models

# Create your models here.

class seoservice(models.Model):
    para1 = models.TextField()
    sol1 = models.TextField()
    sol2 = models.TextField()
    sol3 = models.TextField()
    sol4 = models.TextField()
    img1 = models.ImageField(upload_to='images')
    img2 = models.ImageField(upload_to='images')

class semservice(models.Model):
    para1 = models.TextField()
    sol1 = models.TextField()
    sol2 = models.TextField()
    sol3 = models.TextField()
    sol4 = models.TextField()
    img1 = models.ImageField(upload_to='images')
    img2 = models.ImageField(upload_to='images')

class emailservice(models.Model):
    para1 = models.TextField()
    sol1 = models.TextField()
    sol2 = models.TextField()
    sol3 = models.TextField()
    sol4 = models.TextField()
    img1 = models.ImageField(upload_to='images')
    img2 = models.ImageField(upload_to='images')

class brandingservice(models.Model):
    para1 = models.TextField()
    sol1 = models.TextField()
    sol2 = models.TextField()
    sol3 = models.TextField()
    sol4 = models.TextField()
    img1 = models.ImageField(upload_to='images')
    img2 = models.ImageField(upload_to='images')

class googleservice(models.Model):
    para1 = models.TextField()
    sol1 = models.TextField()
    sol2 = models.TextField()
    sol3 = models.TextField()
    sol4 = models.TextField()
    img1 = models.ImageField(upload_to='images')
    img2 = models.ImageField(upload_to='images')

class facebookservice(models.Model):
    para1 = models.TextField()
    sol1 = models.TextField()
    sol2 = models.TextField()
    sol3 = models.TextField()
    sol4 = models.TextField()
    img1 = models.ImageField(upload_to='images')
    img2 = models.ImageField(upload_to='images')

class influencerservice(models.Model):
    para1 = models.TextField()
    sol1 = models.TextField()
    sol2 = models.TextField()
    sol3 = models.TextField()
    sol4 = models.TextField()
    img1 = models.ImageField(upload_to='images')
    img2 = models.ImageField(upload_to='images')

class contentservice(models.Model):
    para1 = models.TextField()
    sol1 = models.TextField()
    sol2 = models.TextField()
    sol3 = models.TextField()
    sol4 = models.TextField()
    img1 = models.ImageField(upload_to='images')
    img2 = models.ImageField(upload_to='images')

class creativeservice(models.Model):
    para1 = models.TextField()
    sol1 = models.TextField()
    sol2 = models.TextField()
    sol3 = models.TextField()
    sol4 = models.TextField()
    img1 = models.ImageField(upload_to='images')
    img2 = models.ImageField(upload_to='images')

class graphicservice(models.Model):
    para1 = models.TextField()
    sol1 = models.TextField()
    sol2 = models.TextField()
    sol3 = models.TextField()
    sol4 = models.TextField()
    img1 = models.ImageField(upload_to='images')
    img2 = models.ImageField(upload_to='images')

class socialmediamarketingservice(models.Model):
    para1 = models.TextField()
    sol1 = models.TextField()
    sol2 = models.TextField()
    sol3 = models.TextField()
    sol4 = models.TextField()
    img1 = models.ImageField(upload_to='images')
    img2 = models.ImageField(upload_to='images')

class webdesigningservice(models.Model):
    para1 = models.TextField()
    sol1 = models.TextField()
    sol2 = models.TextField()
    sol3 = models.TextField()
    sol4 = models.TextField()
    img1 = models.ImageField(upload_to='images')
    img2 = models.ImageField(upload_to='images')

class contactservice(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()





    