from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics,viewsets
from .serializer import MenuItemSerializers,BookingSerializer
from .models import Menu,Booking
from rest_framework.permissions import IsAuthenticated
# Create your views here.
def index(request):
    return render(request,'index.html',{})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializers

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializers
    
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer