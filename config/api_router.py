from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from mym_services.users.api.views import CompanyViewSet
from mym_services.users.api.views import ContactViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register(r"companies", CompanyViewSet, basename="companies")
router.register(r"contacts", ContactViewSet, basename="contacts")

app_name = "api"
urlpatterns = router.urls
