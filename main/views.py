from django.shortcuts import render
import requests
import json

def home(request):
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":"India"}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "309f7a033cmsh583029db63a7e18p187cc9jsn1ee3fd14a553"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    data = response['response']
    d = data[0]
    print(d)
    context = {
        'all' : d['cases']['total'],
        'recovered' : d['cases']['recovered'],
        'deaths' : d['deaths']['total'],
        'new' : d['cases']['new'],
        'critical' : d['cases']['critical']
    }
    return render(request,'index.html',context)
