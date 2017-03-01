from django.shortcuts import render
from django.http import Http404, JsonResponse
from golfapp.models import Golfscore, ShotPercentages, TotalScores
from .forms import PostForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from golfapp.templatetags.calcs import drive, longiron, approach, chip, putt
from django.db.models import Avg

def homepage(request):
    user = User.objects.all()
    golfscores = Golfscore.objects.all()
    golfscores = golfscores.order_by('-published_date')
    return render(request, 'golfscores/homepage.html', {
        'golfscores': golfscores
    })

def display(request):
    user = User.objects.all()
    golfscores = Golfscore.objects.all()
    golfscores = golfscores.order_by('-published_date')
    current_user = request.user
    fill = TotalScores.objects.filter(author_id=request.user)
    handicap = fill.aggregate(Avg('overunderpar'))
    handicap = handicap['overunderpar__avg']
    return render(request, 'golfscores/display.html', {
        'golfscores': golfscores, 'handicap': handicap
    })

@login_required
def golfscore_entry(request):
    user = User.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            golfscore = form.save(commit=False)
            golfscore.save()
            x = Golfscore.objects.latest('id')
            drivearray = [x.drive1, x.drive2, x.drive3, x.drive4, x.drive5, x.drive6, x.drive7, x.drive8, x.drive9, x.drive10, x.drive11, x.drive12, x.drive13, x.drive14, x.drive15, x.drive16, x.drive17, x.drive18]
            longironarray = [x.longiron1, x.longiron2, x.longiron3, x.longiron4, x.longiron5, x.longiron6, x.longiron7, x.longiron8, x.longiron9, x.longiron10, x.longiron11, x.longiron12, x.longiron13, x.longiron14, x.longiron15, x.longiron16, x.longiron17, x.longiron18]
            approacharray = [x.approach1, x.approach2, x.approach3, x.approach4, x.approach5, x.approach6, x.approach7, x.approach8, x.approach9, x.approach10, x.approach11, x.approach12, x.approach13, x.approach14, x.approach15, x.approach16, x.approach17, x.approach18]
            chiparray = [x.chip1, x.chip2, x.chip3, x.chip4, x.chip5, x.chip6, x.chip7, x.chip8, x.chip9, x.chip10, x.chip11, x.chip12, x.chip13, x.chip14, x.chip15, x.chip16, x.chip17, x.chip18]
            puttarray = [x.putt1, x.putt2, x.putt3, x.putt4, x.putt5, x.putt6, x.putt7, x.putt8, x.putt9, x.putt10, x.putt11, x.putt12, x.putt13, x.putt14, x.putt15, x.putt16, x.putt17, x.putt18]
            courseoutwards = sum([x.par1, x.par2, x.par3, x.par4, x.par5, x.par6, x.par7, x.par8, x.par9])
            courseinwards = sum([x.par10, x.par11, x.par12, x.par13, x.par14, x.par15, x.par16, x.par17, x.par18])
            scoreoutwards = sum([x.score1, x.score2, x.score3, x.score4, x.score5, x.score6, x.score7, x.score8, x.score9])
            scoreinwards = sum([x.score10, x.score11, x.score12, x.score13, x.score14, x.score15, x.score16, x.score17, x.score18])
            a = drivearray.count(True)
            b = drivearray.count(False)
            if a or b is not 0:
                sumvalues1 = (a/(a+b))*100
            else:
                sumvalues1 = 0
            sumvalues1 = round(sumvalues1, 1)
            c = longironarray.count(True)
            d = longironarray.count(False)
            if c or d is not 0:
                sumvalues2 = (c/(c+d))*100
            else:
                sumvalues2 = 0
            sumvalues2 = round(sumvalues2, 1)
            e = approacharray.count(True)
            f = approacharray.count(False)
            if e or f is not 0:
                sumvalues3 = (e/(e+f))*100
            else:
                sumvalues3 = 0
            sumvalues3 = round(sumvalues3, 1)
            g = chiparray.count(True)
            h = chiparray.count(False)
            if g or h is not 0:
                sumvalues4 = (g/(g+h))*100
            else:
                sumvalues4 = 0
            sumvalues4 = round(sumvalues4, 1)
            i = puttarray.count(True)
            j = puttarray.count(False)
            if i or j is not 0:
                sumvalues5 = (i/(i+j))*100
            else:
                sumvalues5 = 0
            sumvalues5 = round(sumvalues5, 1)
            coursepar = courseoutwards + courseinwards
            scoretotal = scoreoutwards + scoreinwards
            overunderpar = scoretotal - coursepar
            r = ShotPercentages(author = x.author, drivepercentage = sumvalues1, longironpercentage = sumvalues2, approachpercentage = sumvalues3, chippercentage = sumvalues4, puttpercentage = sumvalues5)
            s = TotalScores(author = x.author, courseoutwards = courseoutwards, courseinwards = courseinwards, coursepar = coursepar, scoreoutwards = scoreoutwards, scoreinwards = scoreinwards, scoretotal = scoretotal, overunderpar = overunderpar)
            r.save()
            s.save()
            return redirect('display')
    else:
        form = PostForm()
    return render(request, 'golfscores/golfscore_entry.html', {
        'form': form,
    })

@login_required
def golfscore_detail(request, pk):
    golfscores = get_object_or_404(Golfscore, pk=pk)
    return render(request, 'golfscores/golfscore_detail.html', {
        'golfscores': golfscores
    })

@login_required
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

def plot(request, chartID = 'chart_ID', chart_type = 'column', chart_height = 500):
    current_user = request.user
    fill = ShotPercentages.objects.filter(author_id=request.user)
    DR = fill.aggregate(Avg('drivepercentage'))
    DR = DR['drivepercentage__avg']
    LI = fill.aggregate(Avg('longironpercentage'))
    LI = LI['longironpercentage__avg']
    AP = fill.aggregate(Avg('approachpercentage'))
    AP = AP['approachpercentage__avg']
    CH = fill.aggregate(Avg('chippercentage'))
    CH = CH['chippercentage__avg']
    PU = fill.aggregate(Avg('puttpercentage'))
    PU = PU['puttpercentage__avg']

    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    title = {"text": 'Good Shot Percentages'}
    xAxis = {"title": {"text": 'Shot Type'}, "categories": ['Drive', 'Longiron', 'Approach', 'Chip', 'Putt']}
    yAxis = {"title": {"text": 'Percentages (%)'}}
    series = [{"name": 'Average Good Shot Percentage', "data": [DR, LI, AP, CH, PU]}]

    return render(request, 'golfscores/Chart.html', {'chartID': chartID, 'chart': chart,
                                                    'series': series, 'title': title,
                                                    'xAxis': xAxis, 'yAxis': yAxis, 'current_user': current_user})

def plot2(request, chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
    current_user = request.user
    fill = TotalScores.objects.filter(author_id=request.user)
    OUP = list(fill.values_list('overunderpar', flat=True))

    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    title = {"text": 'Scores Over Time'}
    xAxis = {"title": {"text": 'Golfrounds'}, "categories": []}
    yAxis = {"title": {"text": 'Shots over par'}}
    series = [{"name": 'Scores', "data": OUP}]
    return render(request, 'golfscores/Chart2.html', {'chartID': chartID, 'chart': chart,
                                                'series': series, 'title': title,
                                                'xAxis': xAxis, 'yAxis': yAxis, 'current_user': current_user, 'OUP': OUP})

def plot3(request, chartID = 'chart_ID', chartID2 = 'chart_ID2', chart_type = 'column', chart_type2 = 'line', chart_height = 500):
    current_user = request.user
    fill = ShotPercentages.objects.filter(author_id=request.user)
    DR = fill.aggregate(Avg('drivepercentage'))
    DR = DR['drivepercentage__avg']
    LI = fill.aggregate(Avg('longironpercentage'))
    LI = LI['longironpercentage__avg']
    AP = fill.aggregate(Avg('approachpercentage'))
    AP = AP['approachpercentage__avg']
    CH = fill.aggregate(Avg('chippercentage'))
    CH = CH['chippercentage__avg']
    PU = fill.aggregate(Avg('puttpercentage'))
    PU = PU['puttpercentage__avg']

    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    title = {"text": 'Good Shot Percentages'}
    xAxis = {"title": {"text": 'Shot Type'}, "categories": ['Drive', 'Longiron', 'Approach', 'Chip', 'Putt']}
    yAxis = {"title": {"text": 'Percentages (%)'}}
    series = [{"name": 'Average Good Shot Percentage', "data": [DR, LI, AP, CH, PU]}]

    fill = TotalScores.objects.filter(author_id=request.user)
    OUP = list(fill.values_list('overunderpar', flat=True))

    chart2 = {"renderTo": chartID2, "type": chart_type2, "height": chart_height,}
    title2 = {"text": 'Good Shot Percentages'}
    xAxis2 = {"title": {"text": 'Golfrounds'}, "categories": []}
    yAxis2 = {"title": {"text": 'Shots over par'}}
    series2 = [{"name": 'Scores', "data": OUP}]


    return render(request, 'golfscores/Chart3.html', {'chartID': chartID, 'chart': chart,
                                                    'series': series, 'title': title,
                                                    'xAxis': xAxis, 'yAxis': yAxis, 'current_user': current_user,
                                                    'chartID2': chartID2, 'chart2': chart2,
                                                    'series2': series2, 'title2': title2,
                                                    'xAxis2': xAxis2, 'yAxis2': yAxis2,})

def drivingtips(request):
    return render(request, 'golfscores/drivingtips.html', {})

def longirontips(request):
    return render(request, 'golfscores/longirontips.html', {})

def approachtips(request):
    return render(request, 'golfscores/approachtips.html', {})

def chippingtips(request):
    return render(request, 'golfscores/chippingtips.html', {})

def puttingtips(request):
    return render(request, 'golfscores/puttingtips.html', {})
