"""
URL configuration for noteapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import TagViewSet, NotebookViewSet, NoteViewSet, TaggedNoteViewSet, NotebookNoteViewSet
# from . views import UserViewSet

# router = DefaultRouter()
# router.register('users', UserViewSet)

router = routers.DefaultRouter()
router.register(r'tags', TagViewSet)
router.register(r'notebooks', NotebookViewSet)
router.register(r'notes', NoteViewSet)
# router.register(r'tagged_notes', TaggedNoteViewSet, basename='tagged_notes')
# router.register(r'notebook_notes', NotebookNoteViewSet, basename='notebook_notes')

urlpatterns = [
    path('', include(router.urls)),
    path('tags/<int:tag_id>/notes', TaggedNoteViewSet.as_view({'get': 'list'}), name='tagged_notes'),
    path('notebooks/<int:notebook_id>/notes', NotebookNoteViewSet.as_view({'get': 'list'}), name='notebook_notes'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
