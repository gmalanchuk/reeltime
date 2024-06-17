from django.urls import include, path
from rest_framework.routers import DefaultRouter

from tasks import views


router = DefaultRouter()
router.register(prefix="boards", viewset=views.BoardViewSet, basename="board")
router.register(prefix="columns", viewset=views.ColumnViewSet, basename="columns")


urlpatterns = [
    path("", include(router.urls)),
]
