from django.shortcuts import render, redirect

from process.forms import RegistrationForm


# Create your views here.
def showindex(request):
    return render(request, "process_template/home.html")


def registration(request):
    print("____________1______")
    rf = RegistrationForm(request.POST)
    if request.method == "POST":
        print("____________2______")
        if rf.is_valid():
            rf.save()
            return redirect('otp')
        else:
            return render(request, "process_template/registration.html", {"form": rf})
    else:
        return render(request, "process_template/registration.html", {"form": rf})


def otp(request):
    return render(request, 'process_template/otp.html')
