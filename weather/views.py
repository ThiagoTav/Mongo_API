from .bible_verse import main  # Alterado para importar corretamente do módulo atual
from datetime import datetime
from random import randrange
from django.views import View
from django.shortcuts import render, redirect
from .models import WeatherEntity
from .repositories import WeatherRepository
from .serializers import WeatherSerializer

class WeatherView(View):  # Definição de uma nova classe WeatherView para lidar com a visualização do tempo
    def get(self, request):
        verse = main.get_bible_verse()  # Obtendo o versículo da Bíblia
        repository = WeatherRepository(collectionName='weathers')
        weathers = list(repository.getAll())
        serializer = WeatherSerializer(data=weathers, many=True)
        weathersData = []  # Definindo weathersData como uma lista vazia para evitar erros de referência
        if serializer.is_valid():  # Corrigido o uso de parênteses desnecessários
            weathersData = serializer.data
            print(serializer.data)
        else:
            print(serializer.errors)
        return render(request, "home.html", {"weathers": weathersData, "verse": verse})

class WeatherGenerate(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        weather = WeatherEntity(
            temperature=randrange(start=17, stop=40),
            date=datetime.now()
        )
        serializer = WeatherSerializer(data=weather.__dict__)
        if serializer.is_valid():
            serializer.save()  # Salvando o objeto serializado
        else:
            print(serializer.errors)
        return redirect('weather-view')  # Redirecionando para a visualização do tempo

class WeatherReset(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        repository.deleteAll()
        return redirect('weather-view')  # Redirecionando para a visualização do tempo