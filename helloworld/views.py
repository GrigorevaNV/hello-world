from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HomePageView(APIView):

    def get(self, request, *args, **kwargs):
        return Response('Hello World!', status=status.HTTP_200_OK)
