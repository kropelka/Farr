from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import DetailView, ListView
from .models import Firma, Telefon
from .forms import NowaFirmaForm
# Create your views here.

def index(request):
    lista_firm = Firma.objects.all()
    paginator = Paginator(lista_firm, 5)

    page = request.GET.get('page')
    try:
        firmy = paginator.page(page)
    except PageNotAnInteger:
        firmy = paginator.page(1)
    except EmptyPage:
        firmy = paginator.page(paginator.num_pages)

    return render_to_response('index.html', {"firmy" : firmy})

class FirmaDetailView(DetailView):
    model = Firma

class NumeryTelefonowView(ListView):
    model = Telefon

def add_firma(request):
    if request.method == 'POST':
        form = NowaFirmaForm(request.POST)
        if form.is_valid():
                pass
                # ...
    else:
        form = NowaFirmaForm()
    return render(request, 'add_firma.html', {'form': form})





