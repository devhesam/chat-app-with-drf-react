from rest_framework import viewsets, exceptions
from rest_framework.response import Response
from server.models import Server, Category
from server.serializers import ServerSerializer
from django.db.models import Count


# Define a viewset for listing servers.
class SeverListViewSet(viewsets.ViewSet):
    # Initialize the queryset to include all servers.
    queryset = Server.objects.all()

    # Define the list method to handle GET requests.
    def list(self, request):
        # Retrieve query parameters from the request.
        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user") == "true"
        with_num_members = request.query_params.get("with_num_members") == "true"
        by_server_id = request.query_params.get("by_server_id")

        # Check if the request is authenticated if filtering by user or server ID.
        if by_user or by_server_id and not request.user.is_authenticated:
            raise exceptions.AuthenticationFailed()

        # Filter the queryset by category if a category is specified.
        if category:
            self.queryset.filter(category=category)

        # Annotate the queryset with the count of members if requested.
        if with_num_members:
            self.queryset = self.queryset.annotate(member_count=Count("member"))

        # Filter the queryset by the current user if filtering by user.
        if by_user:
            user_id = request.user.id
            self.queryset = self.queryset.filter(member=user_id)

        # Filter the queryset by server ID if specified.
        if by_server_id:
            try:
                self.queryset = self.queryset.filter(id=by_server_id)
            except Server.DoesNotExist:
                raise exceptions.ParseError(f'Server with id {by_server_id} does not exist.')

        # Limit the queryset to a specified quantity if requested.
        if qty:
            self.queryset = self.queryset[: int(qty)]

        # Serialize the queryset and return it in the response.
        serializer = ServerSerializer(self.queryset, many=True, context={"member_count": with_num_members})
        return Response(serializer.data)
