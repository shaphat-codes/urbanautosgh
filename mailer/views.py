from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['POST'])
def order(request):
    if request.method == "POST":
        sender_mail = request.data.get("sender_mail")
        name = request.data.get("name")
        phone = request.data.get("phone")
        vin_number = request.data.get("vin_number")
        issue = request.data.get("issue")
        pickup = request.data.get("pickup")
        
        send_mail("Urban autos request alert!", f" Name: {name} \n Phone: {phone}  \n VIN number: {vin_number} \n Issue description: {issue} \n Pickup and drop off: {pickup}", sender_mail,     ["jehoshaphattatiglo99@gmail.com",])

        return Response("email sent successfully")
