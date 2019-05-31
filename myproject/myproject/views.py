#!/usr/bin/env python
from django.http import HttpResponse
import time

def hello (request):
    return HttpResponse("Hello World! This is my first trial")

def current_time(request):
    return HttpResponse ("Current time is: " + time.strftime('%Y-%m-%d %H: %M: %S'))