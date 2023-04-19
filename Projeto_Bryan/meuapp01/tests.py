from django.test import TestCase
import requests
from django.shortcuts import render

# Create your tests here.
# def home(request):
#     cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
#     cotacao = cotacao.json()
#     cotacao_dolar = cotacao['USDBRL']['bid']
#     cotacao_dolar2 = cotacao_dolar + ";" + cotacao['USDBRL']['create_date']
#     return render(request, 'index.html', {'cotacao_dolar': cotacao_dolar, 'data': cotacao_dolar2})


# def api(request):
#     apidjango = requests.get('http://127.0.0.1:8000/api/?format=json')
#     apidjango = apidjango.json()
#     django_api = apidjango['nome']['codigo']['descricao']
#     apidjango_2 = django_api + ';' + apidjango['nome']['codigo']['descicao']
#     return render(request, 'index.html', {'nome': django_api, 'codigo': apidjango_2})

