from dataclasses import fields

from pyexpat import model
from rest_framework import serializers

from .models import Zone

  class Meta:
    model  = Zone
    fields = '__all__'  
