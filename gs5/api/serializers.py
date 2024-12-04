from rest_framework import serializers
from .models import Student


#validators
def starts_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('value must be r')
    

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators = [starts_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat full')
        return value

    def validate(self, data):
        name = data.get('name')
        city = data.get('city')

        if name.lower() == 'rohit' and city.lower() != 'ranchi':
            raise serializers.ValidationError('city must be ranchi')

        return data