from rest_framework import viewsets, exceptions
from rest_framework.response import Response
from server.models import Server, Category
from server.serializers import ServerSerializer


class SeverListViewSet(viewsets.ViewSet):
    queryset = Server.objects.all()

    def list(self, request):
        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user") == "true"
        by_server_id = request.query_params.get("by_server_id")

        if by_user or by_server_id and not request.user.is_authenticated:
            raise exceptions.AuthenticationFailed()

        if category:
            self.queryset.filter(category=category)

        if by_user:
            user_id = request.user.id
            self.queryset = self.queryset.filter(member=user_id)

        if by_server_id:
            try:
                self.queryset = self.queryset.filter(id=by_server_id)
            except Server.DoesNotExist:
                raise exceptions.ParseError(f'Server with id {by_server_id} does not exist.')

        if qty:
            self.queryset = self.queryset[: int(qty)]

        serializer = ServerSerializer(self.queryset, many=True)
        return Response(serializer.data)
