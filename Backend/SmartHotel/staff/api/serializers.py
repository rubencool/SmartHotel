from rest_framework.serializers import ModelSerializer

from staff.models import Member

class StaffSerializer(ModelSerializer):
	class Meta:
		model = Member
		fields = '__all__'

class StaffCreateSerializer(ModelSerializer):
	class Meta:
		model = Member
		fields = '__all__'