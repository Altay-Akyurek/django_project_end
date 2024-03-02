from django.shortcuts import render
from .models import Hakkimda, Haber, SonBagislar, SSS, Iletisim,Uyelik
from account.models import TreeCertificate

from django.db.models import Count

def hakkında(request):
    hakkimda = Hakkimda.objects.first()  # Retrieve the first record from the Hakkimda model
    return render(request, 'transitions/hakkında.html', {'hakkimda': hakkimda})

def haber(request):
    haber = Haber.objects.all()  # Retrieve all records from the Haber model
    return render(request, 'transitions/haber.html', {'haber': haber})

def son_bagışlar(request):
    son_bagislar = TreeCertificate.objects.all()  # Doğru model adını kullanın
    map = list(TreeCertificate.objects.values('planting_area').annotate(total=Count('planting_area')))
    return render(request, 'transitions/son_bağışlar.html', {'son_bagislar': son_bagislar, 'map' : map})

def sss(request):
    sss_items = SSS.objects.all()  # Retrieve all records from the Hakkimda model
    return render(request, 'transitions/sss.html', {'sss': sss_items})
def iletisim(request):
    iletisim_items = Iletisim.objects.all()  # Retrieve all records from the Iletisim model
    return render(request, 'transitions/iletisim.html', {'iletisim': iletisim_items})
def uyelik(request):
    uyelik_items = Uyelik.objects.all()  # Retrieve all records from the Uyelik model
    return render(request, 'transitions/uyelik.html', {'uyelik': uyelik_items})

def index(request):
    return render(request, 'transitions/index.html')
