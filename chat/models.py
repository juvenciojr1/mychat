from django.db import models
from datetime import datetime

# Create your models here.

class Chat(models.Model):
	data_registro	= models.DateTimeField(auto_now=True)
	usuario 		= models.CharField(max_length = 50, default="") 
	group	 		= models.CharField(max_length = 50, default="") 
	mensagem		= models.CharField(max_length = 1000, default="")