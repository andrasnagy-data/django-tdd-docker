from rest_framework import routers

from .views import MoviesViewSet

router = routers.DefaultRouter()
router.register(r"api/movies", MoviesViewSet, basename="movie")

urlpatterns = router.urls
