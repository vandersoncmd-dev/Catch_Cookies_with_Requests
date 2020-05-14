
from django.shortcuts import render
import json
#Importa o modulo serializers
from django.core import serializers

def home(requests):
    if requests.method == 'GET':
        cookie = requests.headers['Cookie']+'.json'
        try:
            with open(cookie):
                print('Esse arquivo existe!')
        except IOError:
            print('Esse arquivo não existe, sera criado...')
            criar = open(cookie,'w')
            json.dump({},criar)
            criar.close()
    return render(requests,'index.html')

def carrinho(requests):
    dicio = {}
    cookie = requests.headers['Cookie']+'.json'     #Concatenação do cookie + a string '.json'
    if requests.method == 'POST':
        if (requests.POST['codigo'] and requests.POST['item'] !=''):    #Se os inputs codigo e item vinher diferente de vazio, prosiga.
            print("Chave: "+(requests.POST['codigo']))
            print("Valor: "+(requests.POST['item']))
            chave = (requests.POST['codigo'])
            valor = (requests.POST['item'])
            try:    #try, except adicionar informações no cookie proprietario.
                with open(cookie):              #
                    read = open(cookie,'r')     #
                    memoria = json.load(read)   #
                    read.close()                #
                    memoria[chave] = valor      #
                    record = open(cookie,'w')   #Inserindo no Json + informações.
                    json.dump(memoria,record)   #
                    record.close()              #
            except IOError:
                print('Arquivo esta em branco')
    return render (requests, 'carrinho.html',dicio)

