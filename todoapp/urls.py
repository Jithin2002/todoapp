from django.urls import path
from todoapp.views import create_todo,list_all_todos,delete_todo,index,update_todo
urlpatterns=[
    path("create",create_todo,name="create"),
    path('',index,name="home"),
    path("list",list_all_todos,name="list"),
    path("delete/<int:id>",delete_todo,name="delete_todo"),
    path("update/<int:id>",update_todo,name="updatetodo")
]