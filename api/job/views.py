from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from job.models import Job
from job.serializers import JobSerializer

# Create your views here.
@api_view(['GET'])
def getAllJobs(request):

    jobs = Job.objects.all()

    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

