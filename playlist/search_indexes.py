import datetime
from haystack import indexes
from playlist.models import Playlist, Song


class PlaylistIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    date_created = indexes.DateTimeField(model_attr='date_created')
    def get_model(self):
        return Playlist

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(date_created__lte=datetime.datetime.now())


class SongIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    date_created = indexes.DateTimeField(model_attr='date_created')
    
    def get_model(self):
        return Song

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(date_created__lte=datetime.datetime.now())