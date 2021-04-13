from django.http import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Buyer
from .serializers import BuyerSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
import hashlib


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        snippets = Buyer.objects.all()
        serializer = BuyerSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BuyerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BuyerDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Buyer.objects.get(id=pk)
        except Buyer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        buyer = self.get_object(pk)
        serializer = BuyerSerializer(buyer)
        if not (buyer.imei and buyer.serial):
            return Response({"err": 1})

        key = serializer.data['serial']+serializer.data['imei']
        md5 = hashlib.md5(key.encode()).hexdigest()

        new_serializer = {'err': 0,
                          'current_ts': serializer.data['current_ts'],
                          'end_ts': serializer.data['end_ts'],
                          'md5': md5}
        return Response(new_serializer)

    def post(self, request, pk, format=None):
        buyer = self.get_object(pk)
        if buyer.imei and buyer.serial:
            return Response({'err': 1})

        serializer = BuyerSerializer(buyer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            new_serializer = {'err': 0,
                              'current_ts': serializer.data['current_ts'],
                              'end_ts': serializer.data['end_ts'],
                              'md5': serializer.data['md5']}
            return Response(new_serializer)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
