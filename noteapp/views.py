from django.contrib.auth.models import User 

from rest_framework import viewsets
from .models import Note, Tag, Notebook
from .serializers import NoteSerializer, TagSerializer, NotebookSerializer
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

class NotebookViewSet(viewsets.ModelViewSet):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer
    permission_classes = [IsAuthenticated]

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    
class TaggedNoteViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
    def list(self, request, tag_id):
        notes = Note.objects.filter(tags__id=tag_id)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    
class NotebookNoteViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
    def list(self, request, notebook_id):
        notes = Note.objects.filter(notebook_id=notebook_id)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)