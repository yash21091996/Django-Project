from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Company
from .serializers import CompanySerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def company_list(request):
    """
    List all code articles, or create a new Article.
    """
    if request.method == 'GET':
        companys = Company.objects.all()
        serializer = CompanySerializer(companys, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def company_detail(request, pk):
    """
    Retrieve, update or delete article.
    """
    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CompanySerializer(company, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        company.delete()
        return HttpResponse(status=204)

