from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .models import Employee
from .serializers import EmployeeSerializer
from .pagination import StandardResultsSetPagination
from django.db.models import Q
from datetime import datetime


class EmployeeAPIView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get(self, request, pk=None):
        if pk:
            employee = get_object_or_404(Employee, id=pk)
            return Response(EmployeeSerializer(employee).data)

        qs = Employee.objects.all().order_by("id")

        # Filtering
        department = request.GET.get("department")
        role = request.GET.get("role")

        if department:
            qs = qs.filter(department__iexact=department)

        if role:
            qs = qs.filter(role__iexact=role)

        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(qs, request)
        serializer = EmployeeSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        employee = get_object_or_404(Employee, id=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        employee = get_object_or_404(Employee, id=pk)
        employee.delete()
        return Response(status=204)
