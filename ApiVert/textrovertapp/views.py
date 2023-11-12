from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

from .models import TextroVertAppData
from rest_framework.response import Response
from .permissions import IsSuperuserOrReadOnly
from . serializers import TextroVertSerializer


def home(request):
    return render(request, 'textrovertapp/home.html')


class ApiVertViewSet(viewsets.ModelViewSet):
    queryset = TextroVertAppData.objects.all()
    serializer_class = TextroVertSerializer
    permission_classes = [IsSuperuserOrReadOnly]
    renderer_classes = [JSONRenderer]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        # Customize the response format
        formatted_data = {
            "status": "success",
            "message": "Data retrieved successfully",
            "data": serializer.data
        }

        return Response(formatted_data)


class AngerTemplateView(viewsets.ModelViewSet):
    queryset = TextroVertAppData.objects.filter(category='anger')
    serializer_class = TextroVertSerializer
    permission_classes = [IsSuperuserOrReadOnly]

    renderer_classes = [JSONRenderer]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        # Customize the response format
        formatted_data = {
            "status": "success",
            "message": "Data retrieved successfully",
            "data": serializer.data
        }

        return Response(formatted_data)



class BirthdayTemplateView(viewsets.ModelViewSet):
    queryset = TextroVertAppData.objects.filter(category='birthday')
    serializer_class = TextroVertSerializer
    permission_classes = [IsSuperuserOrReadOnly]

    renderer_classes = [JSONRenderer]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        # Customize the response format
        formatted_data = {
            "status": "success",
            "message": "Data retrieved successfully",
            "data": serializer.data
        }

        return Response(formatted_data)


class SadTemplateView(viewsets.ModelViewSet):
    queryset = TextroVertAppData.objects.filter(category='sad')
    serializer_class = TextroVertSerializer
    permission_classes = [IsSuperuserOrReadOnly]

    renderer_classes = [JSONRenderer]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        # Customize the response format
        formatted_data = {
            "status": "success",
            "message": "Data retrieved successfully",
            "data": serializer.data
        }

        return Response(formatted_data)



class LoveTemplateView(viewsets.ModelViewSet):
    queryset = TextroVertAppData.objects.filter(category='love')
    serializer_class = TextroVertSerializer
    permission_classes = [IsSuperuserOrReadOnly]

    renderer_classes = [JSONRenderer]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        # Customize the response format
        formatted_data = {
            "status": "success",
            "message": "Data retrieved successfully",
            "data": serializer.data
        }

        return Response(formatted_data)




class HelpTemplateView(viewsets.ModelViewSet):
    queryset =  TextroVertAppData.objects.filter(category='help')
    serializer_class = TextroVertSerializer
    permission_classes = [IsSuperuserOrReadOnly]

    renderer_classes = [JSONRenderer]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        # Customize the response format
        formatted_data = {
            "status": "success",
            "message": "Data retrieved successfully",
            "data": serializer.data
        }

        return Response(formatted_data)



class HappyTemplateView(viewsets.ModelViewSet):
    queryset = TextroVertAppData.objects.filter(category='happy')
    serializer_class = TextroVertSerializer
    permission_classes = [IsSuperuserOrReadOnly]

    renderer_classes = [JSONRenderer]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        # Customize the response format
        formatted_data = {
            "status": "success",
            "message": "Data retrieved successfully",
            "data": serializer.data
        }

        return Response(formatted_data)



class FearTemplateView(viewsets.ModelViewSet):
    queryset =  TextroVertAppData.objects.filter(category='fear')
    serializer_class = TextroVertSerializer
    permission_classes = [IsSuperuserOrReadOnly]

    renderer_classes = [JSONRenderer]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        # Customize the response format
        formatted_data = {
            "status": "success",
            "message": "Data retrieved successfully",
            "data": serializer.data
        }

        return Response(formatted_data)


class SurpriseTemplateView(viewsets.ModelViewSet):
    queryset = TextroVertAppData.objects.filter(category='surprise')
    serializer_class = TextroVertSerializer
    permission_classes = [IsSuperuserOrReadOnly]

    renderer_classes = [JSONRenderer]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        # Customize the response format
        formatted_data = {
            "status": "success",
            "message": "Data retrieved successfully",
            "data": serializer.data
        }

        return Response(formatted_data)

