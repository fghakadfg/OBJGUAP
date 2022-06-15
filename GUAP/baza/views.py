from django.shortcuts import render
from .models import Articles
from django.views.generic import DetailView
# Create your views here.


def stat_home(request):
    stat = Articles.objects.order_by('-date')[:3]
    return render(request, 'stat/stat_home.html', {'stat':stat})

class StatsDetailView(DetailView):
    model = Articles
    template_name = 'stat/stat_view.html'
    context_object_name = 'article'



