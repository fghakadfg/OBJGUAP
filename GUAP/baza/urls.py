from django.urls import path
from . import views
urlpatterns = [

    path('' , views.stat_home, name='baza_home'),
    path('<int:pk>', views.StatsDetailView.as_view(), name='stat_detail')

]
