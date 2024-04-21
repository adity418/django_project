from django.shortcuts import render
from pasaApp.models import Passenger

# Create your views here.
def passengerdata(request):
    passengers = Passenger.objects.all()
    passDict = {'passengers':passengers}
    return render(request, passDict)