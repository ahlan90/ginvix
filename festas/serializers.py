from rest_framework import serializers

from festas.models import Festa


class FestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Festa
        fields = '__all__'
