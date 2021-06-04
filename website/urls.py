#  website/urls.py
from django.shortcuts import render
from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('', views.index_page_view, name='index'),
    path('ligaEscocesa/', views.liga_escocesa_view, name='ligaEscocesa'),
    path('PremierLeague/', views.premierLeague_view, name='PremierLeague'),
    path('about/', views.about_view, name="about"),
    path('aberdeen/', views.aberdeen_view, name='aberdeen'),
    path('arsenal/', views.arsenal_view, name='arsenal'),
    path('astonVilla/', views.aston_villa_view, name='astonVilla'),
    path('burnley/', views.burnley_view, name='burnley'),
    path('celtic/', views.celtic_view, name='celtic'),
    path('chelsea/', views.chelsea_view, name='chelsea'),
    path('critica/', views.critica_view, name='critica'),
    path('crystalPalace/', views.crystal_palace_view, name='crystalPalace'),
    path('everton/', views.everton_view, name='everton'),
    path('fulham/', views.fulham_view, name='fulham'),
    path('hiberian/', views.hiberian_view, name='hiberian'),
    path('info/', views.info_view, name='info'),
    path('leeds/', views.leeds_view, name='leeds'),
    path('leicester/', views.leicester_view, name='leicester'),
    path('link/', views.links_view, name='link'),
    path('liverpool/', views.liverpool_view, name='liverpool'),
    path('livingston/', views.livingston_view, name='livingston'),
    path('manCity/', views.manCity_view, name='manCity'),
    path('manUnited/', views.manUnited_view, name='manUnited'),
    path('newcastle/', views.newcastle_view, name='newcastle'),
    path('rangers/', views.rangers_view, name='rangers'),
    path('rossCountry/', views.rossCountry_view, name='rossCountry'),
    path('sheffield/', views.sheffield_view, name='sheffield'),
    path('shoutampton/', views.southampton_view, name='southampton'),
    path('spurs/', views.spurs_view, name='spurs'),
    path('westBromwich/', views.west_bromwich_view, name='westBromwich'),
    path('westHam/', views.westHam_view, name='westHam'),
    path('wolves/', views.wolves_view, name='wolves'),
    path('wordcloud/', views.wordcloud_view, name='wordcloud'),
    path('brigton/', views.brighton_view, name='brighton'),
]
