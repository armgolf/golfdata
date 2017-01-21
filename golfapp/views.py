from django.shortcuts import render
from django.http import Http404
from golfapp.models import Golfscore
from .forms import PostForm
from django.shortcuts import redirect, get_object_or_404

def display(request):
    golfscores = Golfscore.objects.all()
    return render(request, 'golfscores/display.html', {
        'golfscores': golfscores,
    })

def golfscore_entry(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            golfscore = form.save(commit=False)
            golfscore.save()
            return redirect('display')
    else:
        form = PostForm()
    return render(request, 'golfscores/golfscore_entry.html', {
        'form': form,
    })

def golfscore_detail(request, pk):
    golfscores = get_object_or_404(Golfscore, pk=pk)
    return render(request, 'golfscores/golfscore_detail.html', {
        'golfscores': golfscores
    })

def golfscore_edit(request, pk):
    golfscore = get_object_or_404(Golfscore, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=golfscore)
        if form.is_valid():
            golfscore = form.save(commit=False)
            golfscore.save()
            return redirect('golfscore_detail', pk=golfscore.pk)
    else:
        form = PostForm(instance=golfscore)
    return render(request, 'golfscores/golfscore_entry.html', {
        'form': form
    })
