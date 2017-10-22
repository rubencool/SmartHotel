from django.contrib import admin
from . models import (
	Category,
	Order,
	Item,
	Table
	)


class CategoryAdmin(admin.ModelAdmin):
	# list_display = ('created_by')
	fieldsets = [
		(None, { 'fields': [('cat_name')] } ),
	]

	def save_model(self, request, obj, form, change):
		if getattr(obj, 'created_by', None) is None:
			obj.created_by = request.user
			obj.save()

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(Table)


