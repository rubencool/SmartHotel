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

# Item Model
class Item(models.Model):
	itm_name = models.CharField(max_length=100)
	rate = models.FloatField()
	details =models.CharField(max_length= 100)
	image_url =models.FilePathField(blank= True, null=True)
	in_category =models.ForeignKey(Category)

	def __str__(self):
		return self.itm_name

#section model
class Section(models.Model):
    section_name = models.CharField(max_length = 10)
    #imgPath = models.CharField(max_length = 30)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    #img = models.FileField(upload_to="uploads")

    def __str__(self):
        return self.section_name

#Table model
class Table(models.Model):
    table_id = models.CharField(max_length = 10)
    section = models.ForeignKey(Section)
    registered = models.BooleanField(default=False)
    checkout = models.BooleanField(default=False)
    cust_id = models.IntegerField(default = 0)

    def __str__(self):
        return self.table_id