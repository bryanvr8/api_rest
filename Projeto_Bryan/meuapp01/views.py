from django.shortcuts import render

def produtos_cadastrados(request):
    return render(request, 'produtos_cadastrados.html')

def login(request):
    return render(request, 'login.html')

def produtos_autenticados(request):
    return render(request, 'produtos_autenticados.html')



