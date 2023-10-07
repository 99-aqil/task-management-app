from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "user",
            "id",
            "title",
            "description",
            "due_date",
            "priority",
            "completed",
            "created_at",
            "updated_at",
            "image",
            "get_image",
            "get_thumbnail",
            "formatted_due_date",
            "formatted_created_at",
            "formatted_updated_at"
        ]