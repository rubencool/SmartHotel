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

from food.models import Category, Item, Table, Section

from .permissions import IsOwnerOrReadOnly

from .serializers import (
	CategorySerializer,
	CategoryCreateSerializer,
	ItemSerializer, TableSerializer,
	SectionSerializer
	)

class CategoryCreateAPIView(CreateAPIView):
	queryset = Category.objects.all()
	serializer_class = CategoryCreateSerializer
	permission_classes = [IsAdminUser]

class CategoryListAPIView(ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


class CategoryDetailAPIView(RetrieveAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class CategoryUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	permission_classes = [IsAdminUser,IsOwnerOrReadOnly]

class CategoryDeleteAPIView(RetrieveDestroyAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

	# item
class ItemCreateAPIView(CreateAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

class ItemListAPIView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer


class ItemDetailAPIView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

class ItemUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

class ItemDeleteAPIView(RetrieveDestroyAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

class CategoryQueryAPIView(ListAPIView):
    serializer_class = ItemSerializer
    lookup_field = 'in_category'
    def get_queryset(self):
        category = self.kwargs["category"]

        return Item.objects.filter(in_category= category)

# Table
class TableCreateAPIView(CreateAPIView):
	queryset = Table.objects.all()
	serializer_class = TableSerializer

class TableListAPIView(ListAPIView):
	queryset = Table.objects.all()
	serializer_class = TableSerializer


class TableDetailAPIView(RetrieveAPIView):
	queryset = Table.objects.all()
	serializer_class = TableSerializer

class TableUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Table.objects.all()
	serializer_class = TableSerializer

class TableDeleteAPIView(RetrieveDestroyAPIView):
	queryset = Table.objects.all()
	serializer_class = TableSerializer

class RegisteredTableAPIView(ListAPIView):
    queryset = Table.objects.filter(registered = True)
    serializer_class = TableSerializer

class UnRegisteredTableAPIView(ListAPIView):
    queryset = Table.objects.filter(registered = False)
    serializer_class = TableSerializer

class CheckoutTableAPIView(ListAPIView):
    queryset = Table.objects.filter(registered = False, checkout = True)
    serializer_class = TableSerializer

class UnCheckoutTableAPIView(ListAPIView):
    queryset = Table.objects.filter(registered = True, checkout = False)
    serializer_class = TableSerializer

class SectionQueryAPIView(ListAPIView):
    serializer_class = TableSerializer
    lookup_field = 'section'
    def get_queryset(self):
        section = self.kwargs["section"]

        return Table.objects.filter(section= section)

class TableIdQueryAPIView(ListAPIView):
    serializer_class = TableSerializer
    lookup_field = 'table_id'
    def get_queryset(self):
        slug = self.kwargs["slug"]

        return Table.objects.filter(table_id= slug)

# section
class SectionCreateAPIView(CreateAPIView):
	queryset = Section.objects.all()
	serializer_class = SectionSerializer

class SectionListAPIView(ListAPIView):
	queryset = Section.objects.all()
	serializer_class = SectionSerializer


class SectionDetailAPIView(RetrieveAPIView):
	queryset = Section.objects.all()
	serializer_class = SectionSerializer

class SectionUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Section.objects.all()
	serializer_class = SectionSerializer

class SectionDeleteAPIView(RetrieveDestroyAPIView):
	queryset = Section.objects.all()
	serializer_class = SectionSerializer