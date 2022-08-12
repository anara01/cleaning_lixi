from django.urls import path
from .views import HomeView, TeamView

urlpatterns = [
	path('', HomeView.as_view(), name='homepage'),
	path('team/', TeamView.as_view(), name='team'),
]