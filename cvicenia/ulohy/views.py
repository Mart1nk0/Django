from django.shortcuts import render, HttpResponse

def ahoj(request):
    return HttpResponse("Ahoj Svet!")

def o_mne(request):
    kontex = {
        "meno":"Martin",
        "vek":17,
        "zaluby": ["skola","matematika","hokej"],
    }
    return render(request,"ulohy/o_mne.html",kontex)

def rozvrh(request):
    hodiny = [
        {"cislo":1, "predmet":"Programovanie"},
        {"cislo":2, "predmet":"Programovanie"},
        {"cislo":3, "predmet":"Matematika"},
        {"cislo":4, "predmet":"Prax"},
        {"cislo":5, "predmet":"Anglický jazyk"},
    ]
    return render(request,"ulohy/rozvrh.html",{"den":"Pondelok", "hodiny":hodiny})
