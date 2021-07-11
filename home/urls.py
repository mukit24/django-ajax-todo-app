from django.urls import path, include
from .views import home_view,create_task,delete_task,edit_task
urlpatterns = [
    path('',home_view,name='home_view'),
    path('add_task/',create_task,name='add_task'),
    path('delete_task/',delete_task,name='delete_task'),
    path('edit_task/',edit_task,name='edit_task'),
]