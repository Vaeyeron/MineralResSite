from django.shortcuts import render, get_object_or_404, redirect
from .models import Mineral


def home(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/home.html', {'minerals': minerals})


def mineral_detail(request, mineral_id):
    mineral = get_object_or_404(Mineral, id=mineral_id)

    show_reserves = True
    if mineral.name == "Цементное сырьё":
        show_reserves = False

    return render(request, 'minerals/mineral_detail.html', {
        'mineral': mineral,
        'show_reserves': show_reserves
    })


def datawrapper_redirect(request, mineral_id, section):
    mineral = get_object_or_404(Mineral, id=mineral_id)
    if section == 'extraction':
        return redirect(mineral.extraction_url)
    elif section == 'reserves':
        return redirect(mineral.reserves_url)
    else:
        return redirect('home')