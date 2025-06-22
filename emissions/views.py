from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class EmissionsView(APIView):
    def get(self, _):
        return Response({ "total_tCO2e": 12450, "projects": 37, "data_quality_pct": 96 })
