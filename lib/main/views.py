# encoding=utf-8
from django.shortcuts import redirect
from django.shortcuts import render

def main(request):
    return render(request, "main/index.html")

def slash(request):
    if request.user.is_authenticated():
        return redirect('map')
    else:
        return render(request, "main/index.html")
