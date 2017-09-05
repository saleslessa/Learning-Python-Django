"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Automobile:

    model = ''
    brand = ''
    year = 0

    def __init__(self):
       model = self.model
       brand = self.brand
       year = self.year

    def MaxPassengers():
        return '0'


class Car(Automobile):
    color = ''

    def __init__(self):
        color = self.color
        model = self.model
        brand = self.brand
        year = self.year

    def MaxPassengers():
        return '5'

class Motocicle(Automobile):
    color = ''
    type = ''

    def __init__(self):
        color = self.color
        type = self.type
        model = self.model
        brand = self.brand
        year = self.year

    def MaxPassengers():
        return '2'