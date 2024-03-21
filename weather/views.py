# views.py

from datetime import datetime
from random import randrange
from django.shortcuts import render, redirect
from django.views import View
from .models import WeatherEntity
from .repositories import WeatherRepository


# views.py

class WeatherGenerate(View):
    def get(self, request):
        repository = WeatherRepository(collectionName='weathers')
        weather_entity = WeatherEntity(
            temperature=randrange(start=17, stop=40),
            date=datetime.now()
        )
        repository.insert(weather_entity.to_dict())
        return redirect('Weather View')
