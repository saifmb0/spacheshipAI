from django.urls import path

from . import views


urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("get_missions/<int:id>", views.get_missions, name="get_missions"),
    path("get_tasks", views.get_tasks, name="get_tasks"),
    path("get_spaceship_info", views.get_spaceship_info, name="get_spaceship_info"),
    path("get_astro_info", views.get_astro_info, name="get_astro_info"),
    path("finish_task", views.finish_task, name="finish_task"),
    path("get_spaceship_data", views.get_spaceship_data, name="get_spaceship_data"),
    path("post_spaceship_data", views.post_spaceship_data, name="post_spaceship_data"),
    path("get_maintenance_history", views.get_maintenance_history, name="get_maintenance_history"),
    path("post_maintenance", views.post_maintenance, name="post_maintenance"),
]