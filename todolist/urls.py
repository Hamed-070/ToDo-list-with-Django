from django.urls import path 
from .views import * 


urlpatterns = [
    path('' , HomePage.as_view() , name='home') , 
    path('add/' , AddTask.as_view() , name='add_task') , 
    path('delete/<int:pk>/' , DeleteTask.as_view() , name='delete_task') , 
    path('update/<int:pk>/' , UpdateTask.as_view() , name='update_task') , 
    path('compeleted/' , compeleted_tasks , name='compeleted_tasks') , 
    path('pending/' , pending_tasks , name='pending_tasks') , 
]








