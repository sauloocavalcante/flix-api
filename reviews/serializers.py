from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

    def validate_stars(self, value):
        if value < 0 or value > 5:
            raise serializers.ValidationError('Escolha um valor entre 0 e 5.')
        return value