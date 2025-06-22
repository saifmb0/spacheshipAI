from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=50, null=True)
    DOB = models.DateField(null=True)
    employment_date = models.DateField(null=True)

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}"

    
class Spaceship(models.Model):
    name = models.CharField(max_length=255)
    data_id = models.ForeignKey("Data", on_delete=models.CASCADE, related_name='spaceships', null=True, blank=True)
    maintenance_id = models.ForeignKey('Maintenance', on_delete=models.CASCADE, related_name='spaceships', null=True, blank=True)
    
    def __str__(self):
        return f"name : {self.name} - data_id : {self.data_id} - maintenance_id {self.maintenance_id}"

class Maintenance(models.Model):
    id = models.AutoField(primary_key=True) 
    date = models.DateField()
    maintainers = models.ManyToManyField(User, related_name='maintained_maintenance_records')
    description = models.TextField()
    spaceship = models.ForeignKey(Spaceship, on_delete=models.CASCADE, related_name='maintenance_history')


    def __str__(self):
        return f"Maintenance {self.id} - {self.date} by {', '.join([user.username for user in self.maintainers.all()])}"

class Mission(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    tasks = models.ManyToManyField("Task", related_name="missions", blank=True)
    astronaut = models.ForeignKey(User, on_delete=models.CASCADE, related_name='missions')
    spaceship = models.ForeignKey("Spaceship", on_delete=models.CASCADE, related_name='missions')

    def __str__(self):
        return f"Mission Name: {self.name}"
    
class Data(models.Model):
    id = models.AutoField(primary_key=True)
    temp = models.FloatField()
    pressure = models.FloatField()
    radiation_level = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    needs_maintenance = models.BooleanField(default=False)
    spaceship = models.ForeignKey(Spaceship, on_delete=models.CASCADE, related_name='data_history')


    def __str__(self):
        return f"Data {self.id} - {self.timestamp} - Maintenance: {self.needs_maintenance}"

class Task(models.Model):

    STATUS = (
        ("Active", "active"),
        ("Finised","finished")
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS, default="Active")
    
    def __str__(self):
        return f"id : {self.id} - title : {self.title} - desc : {self.description} - due_date : {self.due_date}"
