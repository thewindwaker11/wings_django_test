from rest_framework.routers import DefaultRouter

from .views import BookAPIViewset

router = DefaultRouter()
router.register('books', BookAPIViewset)
urlpatterns = router.urls
