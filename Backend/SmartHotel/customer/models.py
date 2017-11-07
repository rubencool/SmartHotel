from django.db import models
from food.models import Table, Item

# Create your models here.
class Customer(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	table_id = models.ForeignKey(Table, blank=True, null=True)

	def __int__(self):
	    return

# Order model
class Order(models.Model):
    cust_id = models.ForeignKey(Customer, blank = True , null=True)
    table_id = models.ForeignKey(Table, blank=True, null=True)
    item = models.CharField(max_length = 30)
    quantity =models.FloatField()
    rate =models.FloatField()
    total =models.FloatField()

    def __str__(self):
        return self.cust_id