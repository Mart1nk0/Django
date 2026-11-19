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


def du3_teplota(request):
    vysledok = None
    jednotka = ''

    if request.method == 'POST':
        teplota = float(request.POST.get('teplota'))
        smer = request.POST.get('smer')

        if smer == 'c_to_f':
            vysledok = teplota * 9 / 5 + 32
            jednotka = '°F'

        elif smer == 'f_to_c':
            vysledok = (teplota - 32) * 5 / 9
            jednotka = '°C'

    return render(request, 'domace/du3_teplota.html', {
        'vysledok': vysledok,
        'jednotka': jednotka
    })
