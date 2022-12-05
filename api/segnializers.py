from rest_framework.serializers import ModelSerializer
from .models import note
class noteSerializers(ModelSerializer):
    class Meta:
        model = note
        fields = ['body', 'updated', 'created']