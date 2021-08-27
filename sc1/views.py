from django.shortcuts import render
from django.views import generic
from .models import Jobs
from .serializers import JobsSerializer

class ListJobsView(generic.ListView):
	queryset = Jobs.objects.all()
	serializer_class = JobsSerializer
	