from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


# def homepage(request):
#     return render(request, "index.html")
from main.models import *


class HomeView(TemplateView):
    template_name = 'main/index.html'


class TeamView(TemplateView):
    """Team"""
    def get(self, request):
        teams = Team.objects.all()
        return render(request, "main/team.html", {"team_list": teams})