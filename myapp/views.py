from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link
from django.http import HttpResponseRedirect, HttpResponse
import csv

# Create your views here.

def scrape(request):
    if request.method == 'POST':
        site = request.POST.get('site', '')
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')

        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Link.objects.create(address=link_address, name=link_text)
        return HttpResponseRedirect('/')
            
    else:
        data = Link.objects.all()

    return render(request, 'myapp/result.html', {'data':data})

def clear(request):
    Link.objects.all().delete()
    return render(request, 'myapp/result.html')

def download(request):
    response = HttpResponse(content_type = 'text/csv')
    response['ContentDisposition'] = 'attachment; filename = "data.csv"'

    writer = csv.writer(response)

    writer.writerow(['ID', 'Name', 'Link'])

    for obj in Link.objects.all():
        writer.writerow([obj.id, obj.name, obj.address])
    
    return response