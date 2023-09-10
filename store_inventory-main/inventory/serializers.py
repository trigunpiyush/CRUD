from rest_framework import serializers
from .models import CuboidBox



class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuboidBox
        fields = ['id','creator','length', 'breadth', 'height','area', 'volume','created_at','updated_at']


class CuboidBoxCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuboidBox
        fields = ('length', 'breadth', 'height')

class CuboidBoxUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuboidBox
        fields = ('length', 'breadth', 'height')



class CuboidBoxListSerializer(serializers.ModelSerializer):
    area = serializers.SerializerMethodField()
    volume = serializers.SerializerMethodField()
    created_by = serializers.SerializerMethodField()
    last_updated = serializers.SerializerMethodField()

    class Meta:
        model = CuboidBox
        fields = ('length', 'breadth', 'height', 'area', 'volume', 'created_by', 'last_updated')

    def get_area(self, obj):
        return obj.length * obj.breadth

    def get_volume(self, obj):
        return obj.length * obj.breadth * obj.height

    def get_created_by(self, obj):
        if self.context['request'].user.is_staff:
            return obj.creator.username
        return None

    def get_last_updated(self, obj):
        if self.context['request'].user.is_staff:
            return obj.updated_at
        return None
