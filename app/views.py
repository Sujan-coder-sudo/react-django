from django.shortcuts import render
from rest_framework.views import APIView
from .models import React
from .serializer import ReactSerializer
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser

class ReactView(APIView):
    # Enable parsing for form data
    parser_classes = [FormParser, MultiPartParser]

    def get(self, request):
        # Fetch and serialize data
        queryset = React.objects.all()
        serializer = ReactSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # Extract employee and department directly from the request
        employee = request.data.get('employee')
        department = request.data.get('department')

        if not employee or not department:
            return Response({"error": "Both 'employee' and 'department' fields are required."}, status=400)
        
        # Create and save the object using the serializer
        data = {'employee': employee, 'department': department}
        serializer = ReactSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
