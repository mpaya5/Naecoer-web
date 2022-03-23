from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
import json
from django.conf import settings
import urllib.request

from studies.models import Studies
def form_valid(self, form):
    # get the token submitted in the form
    recaptcha_response = self.request.POST.get('g-recaptcha-response')
    url = 'https://www.google.com/recaptcha/api/siteverify'
    payload = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    data = urllib.parse.urlencode(payload).encode()
    req = urllib.request.Request(url, data=data)

    # verify the token submitted with the form is valid
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode())

    # result will be a dict containing 'contact' and 'action'.
    # it is important to verify both

    if (not result['contact']) or (not result['action'] == ''):  # make sure action matches the one from your template
        messages.error(self.request, 'Invalid reCAPTCHA. Please try again.')
        return super().form_invalid(form)

# Create your views here.
def home(request):

    if request.method=="POST":
        #     return rendeder(request, "core/thanks.html")
        #Recoger variables del formulario
        subject = request.POST["subject"]
        message = "- Nombre del interesado: " + request.POST["name"] + ". -" + "Email del interesado: " + request.POST["email"] + ". -" + " Con número de teléfono: " + request.POST["phone"] + ". -" + "Mensaje: " + request.POST["message"] 
        email_from = settings.EMAIL_HOST_USER
    
        #Especificar donde va a ir el correo
        recipient_list=["info@naecoer.com"]
        #Activar parámetros
        send_mail(subject, message, email_from, recipient_list)

    #Recoger los Estudios
    studies = Studies.objects.all()
    
    #cargar el template
    return render(request, "core/index.html", {'studies':studies})

def contact(request):

    if request.method=="POST":
            #     return rendeder(request, "core/thanks.html")
        #Recoger variables del formulario
        subject = request.POST["subject"]
        message = "- Nombre del interesado: " + request.POST["name"] + ". -" + "Email del interesado: " + request.POST["email"] + ". -" + " Con número de teléfono: " + request.POST["phone"] + ". -" + "Mensaje: " + request.POST["message"] 
        email_from = settings.EMAIL_HOST_USER
    
        #Especificar donde va a ir el correo
        recipient_list=["info@naecoer.com"]
        #Activar parámetros
        send_mail(subject, message, email_from, recipient_list)

    return render(request, "core/contact.html")

