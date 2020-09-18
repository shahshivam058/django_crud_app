from django.urls import path
from .views import todo_list,todo_detail,todo_create,todo_update,todo_delete


app_name = "todos"

urlpatterns = [
  path("",todo_list,name="todo_list"),
  path("details/<int:id>",todo_detail,name="todo_detail"),
  path("create",todo_create,name="todo_create"),
  path("update/<int:id>",todo_update,name="todo_update"),
  path("delete/<int:id>",todo_delete,name="todo_delete"),
]
