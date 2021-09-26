from rest_framework import serializers

from .models import Statistic


class StatisticSerializer(serializers.ModelSerializer):

    def get_cpc(self, obj):
        return obj.get_cpc()

    def get_cpm(self, obj):
        return obj.get_cpm()

    cpc = serializers.SerializerMethodField()
    cpm = serializers.SerializerMethodField()

    class Meta:
        model = Statistic
        fields = ("id", "date", "views", "clicks", "cost", "cpc", "cpm")
