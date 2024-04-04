from rest_framework import viewsets, exceptions
from rest_framework.response import Response
from server.models import Server, Category
from server.serializers import ServerSerializer
from django.db.models import Count


class SeverListViewSet(viewsets.ViewSet):
    queryset = Server.objects.all()

    def list(self, request):
        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user") == "true"
        with_num_members = request.query_params.get("with_num_members") == "true"
        by_server_id = request.query_params.get("by_server_id")

        if by_user or by_server_id and not request.user.is_authenticated:
            raise exceptions.AuthenticationFailed()

        if category:
            self.queryset.filter(category=category)

        if with_num_members:
            self.queryset = self.queryset.annotate(member_count=Count("member"))

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

        serializer = ServerSerializer(self.queryset, many=True, context={"member_count": with_num_members})
        return Response(serializer.data)
