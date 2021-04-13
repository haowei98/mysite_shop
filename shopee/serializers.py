from rest_framework import serializers
from .models import Buyer
import datetime


class TimestampField(serializers.Field):
    def to_representation(self, value):
        return int(value.timestamp())


class BuyerSerializer(serializers.ModelSerializer):
    end_ts = TimestampField(source="end_date", read_only=True)
    current_ts = serializers.SerializerMethodField('get_timestamp')

    class Meta:
        model = Buyer
        fields = ['id', 'current_ts', 'end_ts', 'serial', 'imei']

    def get_timestamp(self, buyer):
        return int(datetime.datetime.now().timestamp())
