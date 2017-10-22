from rest_framework.generics import (
	CreateAPIView,
	ListAPIView, 
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	RetrieveDestroyAPIView	
	)

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from staff.models import Member

from .permissions import IsOwnerOrReadOnly

from .serializers import (
	StaffSerializer,
	StaffCreateSerializer
	)

class StaffCreateAPIView(CreateAPIView):
	queryset = Member.objects.all()
	serializer_class = StaffCreateSerializer
	permission_classes = [IsAdminUser]

class StaffListAPIView(ListAPIView):
	queryset = Member.objects.all()
	serializer_class = StaffSerializer


class StaffDetailAPIView(RetrieveAPIView):
	queryset = Member.objects.all()
	serializer_class = StaffSerializer

class StaffUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Member.objects.all()
	serializer_class = StaffSerializer
	permission_classes = [IsAdminUser,IsOwnerOrReadOnly]

class StaffDeleteAPIView(RetrieveDestroyAPIView):
	queryset = Member.objects.all()
	serializer_class = StaffSerializer