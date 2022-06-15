from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from api.models import Todo
from django_filters.rest_framework import DjangoFilterBackend


class TodoListCreateAPIView(ListCreateAPIView):
    """
    Listing all todos
    """

    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated,]
    
    # something like params in java
    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter,
        filters.OrderingFilter]

    filterset_fields = ['id', 'title', 'is_complete']
    search_fields = ['title', 'description']
    ordering_fields = ['id']

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    def get_queryset(self):
        return Todo.objects.all().filter(author=self.request.user)


class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Single detail todo
    """
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field = "id"

    def get_queryset(self):
        return Todo.objects.all().filter(author=self.request.user)

# class CreateTodoAPIView(CreateAPIView):
    
#     serializer_class = TodoSerializer
#     permission_classes = [IsAuthenticated,]

#     def perform_create(self, serializer):
#         return serializer.save(author=self.request.user)


# class ListTodoAPIView(ListAPIView):

#     serializer_class = TodoSerializer
#     permission_classes = [IsAuthenticated,]

#     def get_queryset(self):
#         return Todo.objects.all().filter(author=self.request.user)

