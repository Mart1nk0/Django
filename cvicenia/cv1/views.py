from django.http import request
from django.shortcuts import render, HttpResponse

def cv1_index(request):
    kontex = {
        "meno":"Martin Mitka"
    }
    return render(request, "cv1/cv1_index.html", kontex)



def cv1_obchod(request):
    produkty = [
        {"nazov": "Jablko", "cena": 0.5},
        {"nazov": "Banán", "cena": 4.3},
        {"nazov": "Pomaranč", "cena": 2.4},
        {"nazov": "Hruška", "cena": 0.6},
        {"nazov": "Ananás", "cena": 5.4},
    ]


    max_cena = None
    max_cena = request.GET.get('max_cena','')



    if max_cena != "":
        max_cena = float(max_cena)
        produkty = [produkt for produkt in produkty if produkt["cena"] <= max_cena]

    return render(request, "cv1/cv1_obchod.html", {"produkty": produkty})








def cv1_body(request):
    vysledok = None

    if request.method == 'POST':
        body = float(request.POST.get('body'))

        maximum = float(request.POST.get('maximum'))

        percento = (body / maximum) * 100

        if percento >= 90:
            znamka = 1
        elif percento >= 75:
            znamka = 2
        elif percento >= 50:
            znamka = 3
        elif percento >= 30:

            znamka = 4
        else:
            znamka = 5



        vysledok = f"Získali ste {body} bodov z {maximum}, čo je ({percento:.2f})% a vaša známka je {znamka}."


    return render(request, "cv1/cv1_body.html", {"vysledok": vysledok})