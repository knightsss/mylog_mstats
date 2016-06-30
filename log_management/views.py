from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response

def log_management(request):
    return render_to_response('log_management.html')