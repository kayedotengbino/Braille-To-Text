from rest_framework import serializers
from .models import brailleTo

class brailleSerializer(serializers.ModelSerializer):
  class Meta:
    model = brailleTo
    fields = ['id', 'input']