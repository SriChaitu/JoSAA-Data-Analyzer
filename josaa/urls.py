from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='josaa-home'),
    path('start/', views.start,name='josaa-start'),
    path('start/rank/', views.rank_analyser,name='josaa-analyser'),
    path('start/rank/display', views.display,name='josaa-display'),
]