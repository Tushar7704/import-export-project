from django.db import models

class team(models.Model):
    timg=models.URLField(max_length=500)
    tname=models.CharField(max_length=30)

class service(models.Model):
    icon=models.CharField(max_length=100)
    name=models.CharField(max_length=20)
    info=models.TextField(max_length=500)

class AirFreight(models.Model):
    img=models.URLField(max_length=500)
    srvname=models.CharField(max_length=20)
    srvheading=models.CharField(max_length=80)
    srvdetail=models.CharField(max_length=100)
    srvcontant=models.TextField(max_length=500)

class OceanFreight(models.Model):
    img=models.URLField(max_length=500)
    srvname=models.CharField(max_length=20)
    srvheading=models.CharField(max_length=80)
    srvdetail=models.CharField(max_length=100)
    srvcontant=models.TextField(max_length=500)

class LandTransport(models.Model):
    img=models.URLField(max_length=500)
    srvname=models.CharField(max_length=20)
    srvheading=models.CharField(max_length=80)
    srvdetail=models.CharField(max_length=100)
    srvcontant=models.TextField(max_length=500)

class CargoStorage(models.Model):
    img=models.URLField(max_length=500)
    srvname=models.CharField(max_length=20)
    srvheading=models.CharField(max_length=80)
    srvdetail=models.CharField(max_length=100)
    srvcontant=models.TextField(max_length=500)

class client(models.Model):
    img=models.URLField(max_length=500)
    name=models.CharField(max_length=50)
    post=models.CharField(max_length=100)
    info=models.TextField(max_length=500)
# Create your models here.