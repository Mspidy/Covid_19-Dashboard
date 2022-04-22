from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    data=True
    result=None
    globalsummary = None
    countries = None
    while(data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            json=result.json()
            globalsummary =json['Global']
            countries = json['Countries']
            data=False
        except:                                               #not incorrect in infinite loop
            data=True
    return render(request, 'index.html',{'globalsummary':globalsummary,
                                         'countries':countries})