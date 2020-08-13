from django.shortcuts import render
from django.core.mail import send_mail
from .models import seoservice,semservice,socialmediamarketingservice,contentservice,brandingservice,googleservice,graphicservice,influencerservice,facebookservice,creativeservice,webdesigningservice,emailservice

# Create your views here.

def index(request):
    return render(request, "index.html")

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        message = request.POST['message']
        email = request.POST['email']

        send_mail(
            name,
            message,
            email,
            ['gargtanishka04@gmail.com'],
            fail_silently=False
        )

    return render(request, "contact.html")

def successView(request):
    return render(request,"success.html")

def single(request):
    return render(request, "single.html")

def services(request):
    return render(request, "services.html")

def seo(request):
    seoss = seoservice.objects.all()
    return render(request, "seo.html", {'seoss' : seoss})

def influencer(request):
    influencerss = influencerservice.objects.all()
    return render(request, "influencer.html", {'influencerss' : influencerss})

def google(request):
    googless = googleservice.objects.all()
    return render(request, "google.html", {'googless' : googless})

def facebook(request):
    facebookss = facebookservice.objects.all()
    return render(request, "facebook.html", {'facebookss' : facebookss})

def socialmediamarketing(request):
    socialmediamarketingss = socialmediamarketingservice.objects.all()
    return render(request, "socialmediamarketing.html", {'socialmediamarketingss' : socialmediamarketingss})

def branding(request):
    brandingss = brandingservice.objects.all()
    return render(request, "branding.html", {'brandingss' : brandingss})

def creative(request):
    creativess = creativeservice.objects.all()
    return render(request, "creative.html", {'creativess' : creativess})

def graphic(request):
    graphicss = graphicservice.objects.all()
    return render(request, "graphic.html", {'graphicss' : graphicss})

def content(request):
    contentss = contentservice.objects.all()
    return render(request, "content.html", {'contentss' : contentss})

def webdesigning(request):
    webdesigningss = webdesigningservice.objects.all()
    return render(request, "webdesigning.html", {'webdesigningss' : webdesigningss})

def email(request):
    emailss = emailservice.objects.all()
    return render(request, "email.html", {'emailss' : emailss})

def sem(request):
    semss = semservice.objects.all()
    return render(request, "sem.html", {'semss' : semss})