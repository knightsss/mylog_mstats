from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response

def partition_management(request):
    return render_to_response('partition_management.html')