from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def status_check(request):  # noqa
    """Function for checking server state"""
    return Response({"status": "OK"}, status=status.HTTP_200_OK)
