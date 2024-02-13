from rest_framework import serializers
from .models import Note, Notebook, Tag

class NotebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notebook
        fields = ['id', 'name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'notebook', 'tags', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
