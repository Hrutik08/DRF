from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    #validators
    def starts_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('value must be r')
        
    name = serializers.CharField(validators = [starts_with_r])

    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']

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
    
