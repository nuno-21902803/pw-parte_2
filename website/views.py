#  config/views.py
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import UserDForm, UserOpinionForm, QuizzForm
from .models import User_details, Quizz


def quizz_view(request):
    formQuizz = QuizzForm(request.POST or None)
    formQuizz.user_id = request.user.id
    #pontuacao = 0 -> fazer ifs para as respostas e somar se a resposta for igual dps criar uma pagina que motra a pontuacao
    if formQuizz.is_valid():
        formQuizz.save()
        return HttpResponseRedirect(reverse('website:index'))

    context = {'form': formQuizz, 'users_details': User_details.objects.all()}

    return render(request, 'website/quizz.html', context)


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


def crystal_palace_view(request):
    return render(request, "website/Crystal-Palace.html")


def everton_view(request):
    return render(request, "website/everton.html")


def fulham_view(request):
    return render(request, "website/Fulham.html")


def hiberian_view(request):
    return render(request, "website/hibernian.html")


def info_view(request):
    context = {'users_details': User_details.objects.all()}
    return render(request, "website/info.html", context)


def login_view(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
                    request,
                    username=username,
                    password=password
        )

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('website:index'))
        else:
            return render(request, 'website/login.html', {
                "message": 'Credenciais inválidas.'
            })

    return render(request, 'website/login.html')


def edita_user_view(request, user_id):
    user_d = User_details.objects.get(id=user_id)
    form = UserDForm(request.POST or None, instance=user_d)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:index'))

    context = {'form': form, 'user_id': user_id}
    return render(request, 'website/edita.html', context)


def apaga_user_view(request, user_id):
    User_details.objects.get(id=user_id).delete()
    return HttpResponseRedirect(reverse('website:index'))


def critica_view(request):
    form = UserDForm(request.POST or None)
    formOpinion = UserOpinionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:index'))

    if formOpinion.is_valid():
        formOpinion.id_user = request.user.id
        formOpinion.save()
        return HttpResponseRedirect(reverse('website:index'))

    context = {'form': form, 'formOp': formOpinion}

    return render(request, 'website/critica.html', context)


def logout_view(request):
    logout(request)
    return render(request, 'website/index.html')


def leeds_view(request):
    return render(request, "website/leeds.html")


def leicester_view(request):
    return render(request, "website/leicester.html")


def spa_view(request):
    return render(request, "website/spa.html")


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
