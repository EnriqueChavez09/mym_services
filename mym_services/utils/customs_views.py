from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser


class CustomDestroyModelMixin(mixins.DestroyModelMixin):
    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()


class CRUModelViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    pass


class CRUDModelViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    CustomDestroyModelMixin,
):
    pass


class AdminBaseViewSet(viewsets.GenericViewSet):
    permission_classes = (IsAdminUser,)
