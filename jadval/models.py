from urllib import response
from django.db import models
import requests 
import json


class CategoryModel(models.Model):
    name = models.CharField(max_length=200)

    def fetch_exchange_rates(self):
        url = "https://nbu.uz/uz/exchange-rates/json/"
        response = requests.get(url)

         
        # Process the response data here
        if response.status_code == 200:
            exchange_rates = response.json()
           
            # Do something with the exchange rates data
            return exchange_rates
        else:
            # Handle errors if the request fails
            return None
    