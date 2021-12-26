from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def ecom(request):
    return HttpResponse("welcome to yamart online store")
