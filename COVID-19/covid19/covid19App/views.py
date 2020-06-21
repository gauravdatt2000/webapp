from django.shortcuts import render, HttpResponse
import requests
import bs4

# Create your views here.

def index(request):
    url1 = "https://corona-rest-api.herokuapp.com/Api/india"
    country1 = 'india'
    url2 = "https://corona-rest-api.herokuapp.com/Api/usa"
    country2 = 'usa'
    url3 = "https://corona-rest-api.herokuapp.com/Api/italy"
    country3 = 'italy'
    url4 = "https://corona-rest-api.herokuapp.com/Api/spain"
    country4 = 'spain'
    url5 = "https://corona-rest-api.herokuapp.com/Api/France"
    country5 = 'France'
    url6 = "https://corona-rest-api.herokuapp.com/Api/Germany"
    country6 = 'Germany'
    url7 = "https://corona-rest-api.herokuapp.com/Api/UK"
    country7 = 'UK'
    url8 = "https://corona-rest-api.herokuapp.com/Api/China"
    country8 = 'China'
    url9 = "https://corona-rest-api.herokuapp.com/Api/Canada"
    country9 = 'Canada'
    url10 = "https://corona-rest-api.herokuapp.com/Api/Japan"
    country10= 'Japan'
    url11 = "https://corona-rest-api.herokuapp.com/Api/Singapore"
    country11 = 'Singapore'
    url12 = "https://corona-rest-api.herokuapp.com/Api/Australia"
    country12 = 'Australia'

    r = requests.get(url1.format(country1)).json()
    india = {
        'country': r['Success']['country'],
        'cases': r['Success']['cases'],
        'todaycases': r['Success']['todayCases'],
        'todaydeaths': r['Success']['todayDeaths'],
        'deaths' : r['Success']['deaths'],
        'recovered' : r['Success']['recovered']
     }
    r = requests.get(url2.format(country2)).json()
    usa = {
        'country': r['Success']['country'],
        'cases': r['Success']['cases'],
        'todaycases': r['Success']['todayCases'],
        'todaydeaths': r['Success']['todayDeaths'],
        'deaths': r['Success']['deaths'],
        'recovered': r['Success']['recovered']
    }
    r = requests.get(url3.format(country3)).json()
    italy = {
        'country': r['Success']['country'],
        'cases': r['Success']['cases'],
        'todaycases': r['Success']['todayCases'],
        'todaydeaths': r['Success']['todayDeaths'],
        'deaths': r['Success']['deaths'],
        'recovered': r['Success']['recovered']
    }
    r = requests.get(url4.format(country4)).json()
    spain = {
        'country': r['Success']['country'],
        'cases': r['Success']['cases'],
        'todaycases': r['Success']['todayCases'],
        'todaydeaths': r['Success']['todayDeaths'],
        'deaths': r['Success']['deaths'],
        'recovered': r['Success']['recovered']
    }
    r = requests.get(url5.format(country5)).json()
    france = {
        'country': r['Success']['country'],
        'cases': r['Success']['cases'],
        'todaycases': r['Success']['todayCases'],
        'todaydeaths': r['Success']['todayDeaths'],
        'deaths': r['Success']['deaths'],
        'recovered': r['Success']['recovered']
    }
    r = requests.get(url6.format(country6)).json()
    germany = {
        'country': r['Success']['country'],
        'cases': r['Success']['cases'],
        'todaycases': r['Success']['todayCases'],
        'todaydeaths': r['Success']['todayDeaths'],
        'deaths': r['Success']['deaths'],
        'recovered': r['Success']['recovered']
    }
    r = requests.get(url7.format(country7)).json()
    uk = {
        'country': r['Success']['country'],
        'cases': r['Success']['cases'],
        'todaycases': r['Success']['todayCases'],
        'todaydeaths': r['Success']['todayDeaths'],
        'deaths': r['Success']['deaths'],
        'recovered': r['Success']['recovered']
    }
    r = requests.get(url8.format(country8)).json()
    china = {
        'country': r['Success']['country'],
        'cases': r['Success']['cases'],
        'todaycases': r['Success']['todayCases'],
        'todaydeaths': r['Success']['todayDeaths'],
        'deaths': r['Success']['deaths'],
        'recovered': r['Success']['recovered']
    }
    r = requests.get(url9.format(country9)).json()
    canada = {
        'country': r['Success']['country'],
        'cases': r['Success']['cases'],
        'todaycases': r['Success']['todayCases'],
        'todaydeaths': r['Success']['todayDeaths'],
        'deaths': r['Success']['deaths'],
        'recovered': r['Success']['recovered']
    }
    r = requests.get(url10.format(country10)).json()
    japan = {
        'country': r['Success']['country'],
        'cases': r['Success']['cases'],
        'todaycases': r['Success']['todayCases'],
        'todaydeaths': r['Success']['todayDeaths'],
        'deaths': r['Success']['deaths'],
        'recovered': r['Success']['recovered']
    }
    r = requests.get(url11.format(country11)).json()
    singapore = {
        'country': r['Success']['country'],
        'cases': r['Success']['cases'],
        'todaycases': r['Success']['todayCases'],
        'todaydeaths': r['Success']['todayDeaths'],
        'deaths': r['Success']['deaths'],
        'recovered': r['Success']['recovered']
    }
    r = requests.get(url12.format(country12)).json()
    australia = {
        'country': r['Success']['country'],
        'cases': r['Success']['cases'],
        'todaycases': r['Success']['todayCases'],
        'todaydeaths': r['Success']['todayDeaths'],
        'deaths': r['Success']['deaths'],
        'recovered': r['Success']['recovered']
    }


    context = {'ind' : india,
               'us': usa,
               'it': italy,
               'sp': spain,
               'fr': france,
               'ge': germany,
               'uk': uk,
               'ch': china,
               'ca': canada,
               'ja': japan,
               'si': singapore,
               'au': australia
    }

    return render(request,'covid19.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def country(request):
    url = "https://corona-rest-api.herokuapp.com/Api/World"
    country = 'World'

    r = requests.get(url.format(country)).json()

    world = {
        'country': r['Success']['country'],
        'cases': r['Success']['cases'],
        'todaycases': r['Success']['todayCases'],
        'deaths': r['Success']['deaths'],
        'todaydeaths': r['Success']['todayDeaths'],
        'recovered': r['Success']['recovered'],
        'active': r['Success']['active'],
        'critical': r['Success']['critical'],
        'casesPerOneMillion' : r['Success']['casesPerOneMillion'],
        'deathsPerOneMillion': r['Success']['deathsPerOneMillion']
    }

    context = {'w': world}
    return render(request,'country.html',context)