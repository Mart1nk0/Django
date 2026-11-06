from django.shortcuts import render, HttpResponse


def domace(request):
    kontex = {
        "Moje domace ulohy"
    }
    return render(request,"domace/domace.html",kontex)
