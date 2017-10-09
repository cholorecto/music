from rest_framework import serializers
from playlist.models import Playlist


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ('title',)