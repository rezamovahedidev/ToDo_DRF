from django.db import models

# Create your models here.
class ToDo(models.Model):
	title= models.CharField(max_length=120 , blank=True)
	Description= models.TextField(blank=True)
	Date= models.DateField(blank=False)
	completed=models.BooleanField(default= False)

	def __str__(self):
		return self.title