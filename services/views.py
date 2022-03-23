from django.shortcuts import render, get_object_or_404
from .models import Service

from studies.models import Studies

def services(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    #Recoger los estudios
    studies = Studies.objects.all()

    return render(request, "services/sample.html", {'service':service, 'studies':studies})