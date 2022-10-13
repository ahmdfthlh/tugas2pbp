from django.urls import include
from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task
from todolist.views import delete
from todolist.views import update
from todolist.views import show_json
from todolist.views import create_task_ajax
from todolist.views import delete_task_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create_task/', create_task, name='create_task'),
    path('delete/<int:id>', delete, name='delete'),
    path('update/<int:id>', update, name='update'),
    path('json/', show_json, name='show_json'),
    path('add/', create_task_ajax, name='create_task_ajax'),
    path('delete/<int:id>/', delete_task_ajax, name="delete_task_ajax"),
]
