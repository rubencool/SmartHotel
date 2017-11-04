from django.db import models
from django.contrib.auth.models import User
from staff.models import Member

# Create your models here.
class Category(models.Model):
	cat_name = models.CharField(max_length = 25)
	created_by = models.ForeignKey(User, null=True, blank=True)
	icon = models.CharField(max_length = 25)

	def __str__(self):
		return self.cat_name

# Order model
class Order(models.Model):
	table_no = models.ForeignKey("Table")
	item = models.ForeignKey("Item")
	quantity =models.FloatField()
	which_waiter = models.ForeignKey(Member, blank=True, null=True)

	def __int__(self):
		return self.id

# Item Model
class Item(models.Model):
	itm_name = models.CharField(max_length=100)
	rate = models.FloatField()
	details =models.CharField(max_length= 100)
	image_url =models.FilePathField(blank= True, null=True)
	in_category =models.ForeignKey(Category)

	def __str__(self):
		return self.itm_name



#Table model
class Table(models.Model):
    tabel_Id = models.CharField(max_length = 10)
    section = models.CharField(max_length = 100)
    registered = models.BooleanField(default=False)

    def __str__(self):
        return self.section