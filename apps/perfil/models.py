# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Me(models.Model):
	my_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length = 25)
	last_name = models.CharField(max_length = 35)
	email = models.EmailField()
	fecha = models.DateTimeField() 
	sexo = models.CharField(max_length = 12)
	user = models.CharField(max_length = 25)
	psswd = models.CharField(max_length = 30)

class Amistad(models.Model):
	amigo_id = models.AutoField(primary_key = True)
	my_id = models.ForeignKey(Me, null=True, blank=True, on_delete=models.CASCADE)

class My_perfil(models.Model):
	perfil_id = models.AutoField(primary_key = True)
	my_id = models.OneToOneField(Me, null=True, blank=True, on_delete=models.CASCADE)
	color = models.CharField(max_length = 25)

class Fotos(models.Model):
	foto_if = models.ImageField(upload_to = 'photo')
	perfil_id = models.ForeignKey(My_perfil, null = True, blank = True, on_delete = models.CASCADE)

class My_blog(models.Model):
	blog_id = models.AutoField(primary_key = True)
	fecha_publi = models.DateTimeField()
	detalle = models.TextField()
	amigo_id = models.ForeignKey(Amistad, null = True, blank = True, on_delete = models.CASCADE)
	perfil_id = models.ForeignKey(My_perfil, null = True, blank = True, on_delete = models.CASCADE)
	
		