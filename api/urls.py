# from api.views import CreateTodoAPIView, ListTodoAPIView
from api.views import TodoListCreateAPIView, TodoDetailAPIView
from django.urls import path


urlpatterns = [
    # path('create', CreateTodoAPIView.as_view(), name="create-todo"),
    # path('list', ListTodoAPIView.as_view(), name="list-todo"),
    path('', TodoListCreateAPIView.as_view(), name="todos"),
    path('<int:id>', TodoDetailAPIView.as_view(), name="detail"),
]