# import necessary libraries
from django.db.models import Q
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from django.contrib.auth.mixins import LoginRequiredMixin

# import serializers
from .serializers import TaskSerializer

# import models
from .models import Task


class ListTaskAPI(LoginRequiredMixin, APIView):
    
    def get(self, request):
        tasks = Task.objects.filter(user=self.request.user)
        serializer = TaskSerializer(tasks, many=True)

        return render(request, 'task_view.html', {'tasks': serializer.data})
    
        # return Response(serializer.data)


class AddTaskAPI(LoginRequiredMixin, APIView):
    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('list-task')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DetailTaskAPI(LoginRequiredMixin, APIView):
    
    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)


class EditTaskAPI(APIView):
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteTaskAPI(APIView):
    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TaskSearchAPI(APIView):

    def get(self, request):
        search_query = request.query_params.get('search', '')
        tasks = Task.objects.filter(title__icontains=search_query, user=request.user)
        serializer = TaskSerializer(tasks, many=True)

        return render(request, 'search.html', {'tasks': serializer.data, 'query': search_query})

        # return Response(serializer.data, status=status.HTTP_200_OK)
