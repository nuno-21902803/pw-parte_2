#  config/views.py
from django.http import HttpResponse
from django.shortcuts import render


def index_page_view(request):
    return render(request, "website/index.html")


def liga_escocesa_view(request):
    return render(request, "website/ligaEscocesa.html")


def aberdeen_view(request):
    return render(request, "website/aberdeen.html")


def about_view(request):
    return render(request, "website/about.html")


def arsenal_view(request):
    return render(request, "website/arsenal.html")


def aston_villa_view(request):
    return render(request, "website/aston-villa.html")


def brighton_view(request):
    return render(request, "website/brigton.html")


def burnley_view(request):
    return render(request, "website/Burnley.html")


def celtic_view(request):
    return render(request, "website/celtic.html")


def chelsea_view(request):
    return render(request, "website/chelsea.html")


def critica_view(request):
    return render(request, "website/critica.html")


def crystal_palace_view(request):
    return render(request, "website/Crystal-Palace.html")


def everton_view(request):
    return render(request, "website/everton.html")


def fulham_view(request):
    return render(request, "website/Fulham.html")


def hiberian_view(request):
    return render(request, "website/hibernian.html")


def info_view(request):
    return render(request, "website/info.html")


def leeds_view(request):
    return render(request, "website/leeds.html")


def leicester_view(request):
    return render(request, "website/leicester.html")


def links_view(request):
    return render(request, "website/links.html")


def liverpool_view(request):
    return render(request, "website/liverpool.html")


def livingston_view(request):
    return render(request, "website/livingston.html")


def manCity_view(request):
    return render(request, "website/manCity.html")


def manUnited_view(request):
    return render(request, "website/manUnited.html")


def newcastle_view(request):
    return render(request, "website/Newcastle.html")


def premierLeague_view(request):
    return render(request, "website/premierLeague.html")


def rangers_view(request):
    return render(request, "website/rangers.html")


def rossCountry_view(request):
    return render(request, "website/rossCounty.html")


def sheffield_view(request):
    return render(request, "website/Sheffield.html")


def southampton_view(request):
    return render(request, "website/southampton.html")


def spurs_view(request):
    return render(request, "website/spurs.html")


def west_bromwich_view(request):
    return render(request, "website/West-Bromwich.html")


def wolves_view(request):
    return render(request, "website/wolves.html")


def wordcloud_view(request):
    return render(request, "website/wordcloud.html")


def westHam_view(request):
    return render(request, "website/west-ham.html")