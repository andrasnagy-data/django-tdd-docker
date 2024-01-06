from rest_framework.viewsets import ModelViewSet

from .models import Movie
from .serializers import MovieSerializer


class MoviesViewSet(ModelViewSet):
    """
    A viewset for viewing and editing movie instances.
    """

    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
