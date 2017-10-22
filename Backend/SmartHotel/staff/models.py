from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#Staff Model
class Member(models.Model):
	first_name = models.CharField(max_length = 25)
	last_name = models.CharField(max_length = 25)
	address = models.CharField(max_length = 25)
	email = models.EmailField(null= True, blank= True)
	is_manager = models.BooleanField(default = False)
	is_active = models.BooleanField(default = False)
	is_waiter = models.BooleanField(default = False)
	created_by = models.ForeignKey(User, null=True, blank=True)

	def __str__(self):
		return self.first_name
