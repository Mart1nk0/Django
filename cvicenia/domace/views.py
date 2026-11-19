from django.shortcuts import render, HttpResponse


def domace(request):
    kontex = {
        "Moje domace ulohy"
    }
    return render(request,"domace/domace.html",kontex)


def du2_vizitka(request):
    vizitka = {
        'meno': 'Martin Mitka',
        'trieda': '3.AT',
        'vek': 17,
        'predmety': [
            'Programovanie',
            'Telesná výchova',
            'Anglický jazyk'
        ]
    }

    return render(request, 'domace/du2_vizitka.html', {
        'vizitka': vizitka
    })
