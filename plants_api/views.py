from rest_framework import status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from plants_api.models import Plant
from plants_api.serializers import PlantFullSerializer, PlantListSerializer


class LimitPageNumberPagination(PageNumberPagination):
    page_size_query_param = "limit"
    max_page_size = 100


class PlantViewSet(viewsets.ModelViewSet):
    """API endpoint for events."""
    queryset = Plant.objects.all()
    pagination_class = LimitPageNumberPagination

    def get_serializer_class(self):
        if self.action == "list":
            return PlantListSerializer

        return PlantFullSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)