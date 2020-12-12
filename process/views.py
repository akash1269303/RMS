from django.shortcuts import render
from process
# Create your views here.
def showindex(request):
    return render(request, "process_template/home.html")

def registration(request):
    return render(request,"process_template/registration.html")