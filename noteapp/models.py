from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Notebook(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.notebook:
            default_notebook, _ = Notebook.objects.get_or_create(name='Default Notebook')
            self.notebook = default_notebook
        super().save(*args, **kwargs)