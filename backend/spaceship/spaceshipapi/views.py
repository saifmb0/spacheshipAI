from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework import status


from .serializers import MissionSerializer, TasksSerializer, SapceshipSerializer, AstronautSerializer, DataSerializer, MaintenanceSerializer
from .models import Spaceship, Data, Mission, User

# Create your views here.

@api_view(["POST"])
def login_user(request):
    username = request.data.get("username")  
    password = request.data.get("password")  

    print(f"username: {username}, password: {password}")

    user = authenticate(username=username, password=password)
    
    print(user)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, "user_id": user.id}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET"])
def get_missions(request, id):
    print(id)
    missions = Mission.objects.filter(astronaut=id)

    print(missions)

    if missions.exists():
        # Converts Django datatypes to JSON to send over API
        serializer = MissionSerializer(missions, many=True)
        return Response({'missions': serializer.data}, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_tasks(request):
    
    mission_id = request.data.get("mission_id")
    spaceship_id = request.data.get("spaceship_id")


    mission = Mission.objects.filter(id=mission_id, astronaut=request.user, spaceship=spaceship_id).first()

    if mission.exists():
        # Get the mission's tasks through related name
        tasks = mission.tasks.all()
        serializer = TasksSerializer(tasks, many=True)
        return Response({"tasks": serializer.data}, status=status.HTTP_200_OK)
    

@api_view(["GET"])
def get_spaceship_info(request):
    spaceship = Spaceship.objects.filter() # TO-DO

    if spaceship.exists():
        serializer = SapceshipSerializer(spaceship)
        return Response({'missions': serializer.data}, status=status.HTTP_200_OK)
    

@api_view(["GET"])
def get_astro_info(request):
    astro = User.objects.filter(user=request.user)

    if astro.exists():
        serializer = AstronautSerializer(astro)
        return Response({"astro": serializer.data}, status=status.HTTP_200_OK)
    

@api_view(["POST"])
def finish_task(request):

    serializer = TasksSerializer(request.data)

    if serializer.is_valid():
        
        # Get the task object from validated data
        task = serializer.save()

        # Update the status to "Finished"
        task.status = "Finished"
        task.save()

        return Response({"success": "Task status updated to Finished"}, status=status.HTTP_201_CREATED)

@api_view(["GET"])
def get_spaceship_data(request):

    data = Data.objects.filter(spaceship=request.user.spaceship_profile)

    if data.exists():
        serializer = DataSerializer(data, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

@api_view(["POST"])
def post_spaceship_data(request):

    serializer = DataSerializer(data=request.data)

    if serializer.is_valid():  # This will validate the data automatically
        serializer.save()  # This will create the new Data object
        return Response({"success": "Data entry created successfully."}, status=status.HTTP_201_CREATED)

@api_view(["GET"])
def get_maintenance_history(request):

    # Get all maintenance records for a specific spaceship
    spaceship = Spaceship.objects.get(id=request.user.spaceship_profile)
    spaceship_maintenance = spaceship.maintenance_history.all()

    if spaceship_maintenance.exists():
        serializer = MaintenanceSerializer(spaceship_maintenance)
        return Response({'missions': serializer.data}, status=status.HTTP_200_OK)



@api_view(["POST"])
def post_maintenance(request):
    # Validate the incoming data with the serializer
    serializer = MaintenanceSerializer(data=request.data)
    
    if serializer.is_valid():

        # Get spaceship from the request
        spaceship_id = request.data.get("spaceship")
        maintainer_ids = request.data.get("maintainers", [])  # List of astronaut IDs

        spaceship = Spaceship.objects.get(id=spaceship_id)
        # Retrieve the list of maintainers (astronauts)
        maintainers = User.objects.filter(id__in=maintainer_ids)

        if maintainers.exists():
            # Create and save the Maintenance object
            maintenance = serializer.save(spaceship=spaceship)
            maintenance.maintainers.set(maintainers)  # Associate multiple maintainers

            # Return a response with the serialized data of the created Maintenance object
            return Response({"maintenance": serializer.data}, status=status.HTTP_201_CREATED)

