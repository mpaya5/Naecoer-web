from django.shortcuts import render
from .models import Studies

# Create your views here.
def studies(request):
    studies = Studies.objects.all()
    return render(request, "studies/studies.html" , {'studies':studies})