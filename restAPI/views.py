from django.shortcuts import render
from .models import Task
from .serializer import TaskSerializer
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view



class TaskListCreateAPIView(APIView):
    """
    View to list all tasks and create a new task.
    """

    def get(self, request):
        # Retrieve all tasks
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Create a new task
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class TaskDetailAPIView(APIView):
    """
    View to retrieve, update, and delete a specific task.
    """

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return None

    def get(self, request, pk):
        # Retrieve a specific task
        task = self.get_object(pk)
        if not task:
            return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        # Update a specific task
        task = self.get_object(pk)
        if not task:
            return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Delete a specific task
        task = self.get_object(pk)
        if not task:
            return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
