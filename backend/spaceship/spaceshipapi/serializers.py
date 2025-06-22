from rest_framework import serializers
from .models import Mission, Task, Spaceship, Data, Maintenance, User

class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = [
            'id',
            'name',
            'start_date',
            'end_date',
            'tasks'
        ]


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "due_date",
            "status"
        ]



class SapceshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spaceship
        fields = ["id", "name"]



class AstronautSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "DOB",
            "employment_date"
        ]


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = [
            "temp",
            "pressure",
            "radiationlevel",
            "timestamp",
            "needs_maintenance"
        ]   


class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = ['id', 'date', 'maintainers', 'description', 'spaceship']