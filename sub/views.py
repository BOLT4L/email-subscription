from django.shortcuts import render , redirect
from django.contrib import messages
from django.http import HttpResponse , JsonResponse
from .models import sub
# Create your views here.
def index(request):
    if request.method == 'POST' :
          mail = request.POST['emails']
          user =sub.objects.create(mail=mail)
          user.save()
          messages.info(request,'registered successful')
    return render(request , 'index.html')