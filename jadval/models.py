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


class PediatryaModel(models.Model):
    faculty = models.CharField(max_length=200)
    kurs_1 = models.CharField(max_length=100)
    kurs_id_1 = models.IntegerField()

    kurs_2 = models.CharField(max_length=100)
    kurs_id_2 = models.IntegerField()

    kurs_3 = models.CharField(max_length=100)
    kurs_id_3 = models.IntegerField()

    kurs_4 = models.CharField(max_length=100)
    kurs_id_4 = models.IntegerField()

    kurs_5 = models.CharField(max_length=100)
    kurs_id_5 = models.IntegerField()

    kurs_6 = models.CharField(max_length=100)
    kurs_id_6 = models.IntegerField()



    def __str__(self):
        return (f" {self.faculty} "
                f"{self.kurs_1}"
                f"  {self.kurs_2}"
                f" {self.kurs_3} "
                f"{self.kurs_4} "
                f"{self.kurs_5} "
                f"{self.kurs_6}")
