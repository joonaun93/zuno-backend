from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date, timedelta
import random

class EmissionsView(APIView):
    def get(self, _):


        today = date.today()
        data = []

        for i in range(12):
            month = (today.replace(day=1) - timedelta(days=30 * i)).strftime("%Y-%m")
            data.append({
                "month": month,
                "s1": random.randint(900, 1100),
                "s2": random.randint(600, 800),
                "s3": random.randint(4500, 5500),
            })

        data.reverse()

        return Response({ "total_tCO2e": 12450, "projects": 37, "data_quality_pct": 96, "data": data })



