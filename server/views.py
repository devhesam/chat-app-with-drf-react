from rest_framework import viewsets
from rest_framework.response import Response
from server.models import Server, Category
from server.serializers import ServerSerializer


class SeverListViewSet(viewsets.ViewSet):
    queryset = Server.objects.all()

    def list(self, request):
        category = request.query_params.get("category")
        if category:
            self.queryset.filter(category=category)
        serializer = ServerSerializer(self.queryset, many=True)
        return Response(serializer.data)
