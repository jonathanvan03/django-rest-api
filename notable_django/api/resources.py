from tastypie.resources import ModelResource
from api.models import Note
from tastypie.authorization import Authorization

class NoteResource(ModelResource): 
    class Meta:
        queryset = Note.objects.all()
        resource_namne = 'note'
        authorization = Authorization()
        fields = ['title', 'body']

