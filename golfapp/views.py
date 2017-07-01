from django.shortcuts import render
from django.http import Http404, JsonResponse
from golfapp.models import Golfscore, ShotPercentages, TotalScores, GolfCourses, Leaguetable, Signup
from .forms import PostForm, gcselection, PNumber
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from golfapp.templatetags.calcs import drive, longiron, approach, chip, putt
from django.db.models import Avg

def privacy(request):
    return render(request, 'golfscores/privacy.html', {})

def leaguerules(request):
    return render(request, 'golfscores/leaguerules.html', {})

def landingpage(request):
    return render(request, 'golfscores/landingpage.html', {})

@login_required
def leaguetable(request):
    leaguetable = Leaguetable.objects.all()
    leaguetable = leaguetable.order_by('-points', '-played')
    golfscore = Golfscore.objects.all()
    golfscore = golfscore.order_by('-pk')
    totalscores = TotalScores.objects.all()
    totalscores = totalscores.order_by('-pk')
    combolist = zip(totalscores, golfscore)
    user = User.objects.all()
    current_user = request.user
    nextleague = Signup.objects.all()
    signup = Signup.objects.filter(author=current_user)
    if signup.exists():
        signup = 1
    else:
        signup = 0
    if request.method == "POST":
        form = PNumber(request.POST)
        if form.is_valid():
            signedupuser = Signup.objects.create(author=current_user, phonenumber=(request.POST.get('phonenumber')))
            signup = Signup.objects.filter(author=current_user)
            if signup.exists():
                signup = 1
            else:
                signup = 0
            return render(request, 'golfscores/leaguetable.html', {
                'leaguetable': leaguetable, 'golfscore': golfscore, 'totalscores': totalscores,'combolist': combolist, 'signup': signup, 'nextleague': nextleague,
            })
    else:
        form = PNumber()
    return render(request, 'golfscores/leaguetable.html', {
        'leaguetable': leaguetable, 'golfscore': golfscore, 'totalscores': totalscores,'combolist': combolist, 'signup': signup, 'nextleague': nextleague, 'form': form,
    })

def homepage(request):
    golfscores = Golfscore.objects.all()
    golfscores = golfscores.order_by('-pk')
    totalscores = TotalScores.objects.all()
    totalscores = totalscores.order_by('-pk')
    shotpercentages = ShotPercentages.objects.all()
    shotpercentages = shotpercentages.order_by('-pk')
    combolist = zip(totalscores, shotpercentages, golfscores)
    leaguetable = Leaguetable.objects.all()
    leaguetable = leaguetable.order_by('-points', '-played')
    return render(request, 'golfscores/homepage.html', {
        'totalscores': totalscores, 'shotpercentages': shotpercentages, 'combolist': combolist, 'golfscores': golfscores, 'leaguetable': leaguetable,
    })

@login_required
def display(request):
    user = User.objects.all()
    golfscores = Golfscore.objects.all()
    golfscores = golfscores.order_by('-pk')
    totalscores = TotalScores.objects.all()
    totalscores = totalscores.order_by('-pk')
    shotpercentages = ShotPercentages.objects.all()
    shotpercentages = shotpercentages.order_by('-pk')
    combolist = zip(totalscores, shotpercentages, golfscores)
    current_user = request.user
    fill = TotalScores.objects.filter(author_id=request.user).order_by('-pk')[:5]
    handicap = fill.aggregate(Avg('overunderpar'))
    handicap = handicap['overunderpar__avg']
    currentuser = request.user
    noofscores= Golfscore.objects.filter(author=currentuser).count()
    return render(request, 'golfscores/display.html', {
        'totalscores': totalscores, 'shotpercentages': shotpercentages, 'handicap': handicap, 'combolist': combolist, 'golfscores': golfscores, 'noofscores': noofscores,
    })

@login_required
def golfscore_preentry(request):
    user = User.objects.all()
    if request.method == 'POST':
        form = gcselection(request.POST)
        if form.is_valid():
            golfcourse = GolfCourses.objects.get(course=(request.POST.get('field1')))
            golfscore = Golfscore(course=golfcourse, author=request.user)
            golfscore.save()
            g = Golfscore.objects.latest('id')
            totalscores = TotalScores(pk=g.pk)
            shotpercentages = ShotPercentages(pk=g.pk)
            totalscores.save()
            shotpercentages.save()
            return redirect('scoresave')
    else:
        form = gcselection()
    return render(request, 'golfscores/golfscore_preentry.html', {
        'form': form
    })

@login_required
def scoresave(request):
    user = User.objects.all()
    golfscore = Golfscore.objects.latest('id')
    golfcourse = golfscore.course
    coursedata = GolfCourses.objects.filter(course=golfcourse)
    if request.method == "POST":
        form = PostForm(request.POST, instance=golfscore)
        if form.is_valid():
            golfscore = form.save(commit=False)
            golfscore.save()
            x = Golfscore.objects.latest('id')
            y = GolfCourses.objects.get(course=x.course)
            drivearray = [x.drive1, x.drive2, x.drive3, x.drive4, x.drive5, x.drive6, x.drive7, x.drive8, x.drive9, x.drive10, x.drive11, x.drive12, x.drive13, x.drive14, x.drive15, x.drive16, x.drive17, x.drive18]
            longironarray = [x.longiron1, x.longiron2, x.longiron3, x.longiron4, x.longiron5, x.longiron6, x.longiron7, x.longiron8, x.longiron9, x.longiron10, x.longiron11, x.longiron12, x.longiron13, x.longiron14, x.longiron15, x.longiron16, x.longiron17, x.longiron18]
            approacharray = [x.approach1, x.approach2, x.approach3, x.approach4, x.approach5, x.approach6, x.approach7, x.approach8, x.approach9, x.approach10, x.approach11, x.approach12, x.approach13, x.approach14, x.approach15, x.approach16, x.approach17, x.approach18]
            chiparray = [x.chip1, x.chip2, x.chip3, x.chip4, x.chip5, x.chip6, x.chip7, x.chip8, x.chip9, x.chip10, x.chip11, x.chip12, x.chip13, x.chip14, x.chip15, x.chip16, x.chip17, x.chip18]
            puttarray = [x.putt1, x.putt2, x.putt3, x.putt4, x.putt5, x.putt6, x.putt7, x.putt8, x.putt9, x.putt10, x.putt11, x.putt12, x.putt13, x.putt14, x.putt15, x.putt16, x.putt17, x.putt18]
            courseoutwards = sum([y.par1, y.par2, y.par3, y.par4, y.par5, y.par6, y.par7, y.par8, y.par9])
            courseinwards = sum([y.par10, y.par11, y.par12, y.par13, y.par14, y.par15, y.par16, y.par17, y.par18])
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
            r = ShotPercentages.objects.latest('id')
            s = TotalScores.objects.latest('id')
            r = ShotPercentages(author = x.author, drivepercentage = sumvalues1, longironpercentage = sumvalues2, approachpercentage = sumvalues3, chippercentage = sumvalues4, puttpercentage = sumvalues5, course = x.course, pk=x.pk)
            s = TotalScores(author = x.author, courseoutwards = courseoutwards, courseinwards = courseinwards, coursepar = coursepar, scoreoutwards = scoreoutwards, scoreinwards = scoreinwards, scoretotal = scoretotal, overunderpar = overunderpar, course = x.course, pk=x.pk)
            r.save()
            s.save()
            x = Golfscore.objects.latest('id')
            s = TotalScores.objects.latest('id')
            if x.o1totalscore != None:
                myscore = s.scoretotal
                array = [x.o1totalscore, x.o2totalscore, x.o3totalscore]
                array = [item for item in array if item is not None]
                wins = sum(item>myscore for item in array)
                losses = sum(item<myscore for item in array)
                draws = sum(item==myscore for item in array)
                lt = Leaguetable.objects.filter(player=x.author)
                lt = list(lt[:1])
                lt = lt[0]
                newwon = lt.won + wins
                newdrawn = lt.drawn + draws
                newlost = lt.lost + losses
                newpoints = lt.points + ((wins*2)+draws)
                newplayed = (newwon + newlost + newdrawn)
                t = Leaguetable(pk=lt.pk, won=newwon, lost=newlost, drawn=newdrawn, points=newpoints, player=lt.player, played=newplayed)
                t.save()
                return redirect('display')
            else:
                return redirect('display')
    else:
        form = PostForm({
            'score1':golfcourse.par1,'score2':golfcourse.par2,'score3':golfcourse.par3,
            'score4':golfcourse.par4,'score5':golfcourse.par5,'score6':golfcourse.par6,
            'score7':golfcourse.par7,'score8':golfcourse.par8,'score9':golfcourse.par9, 'score10':golfcourse.par10,
            'score11':golfcourse.par11,'score12':golfcourse.par12,'score13':golfcourse.par13,
            'score14':golfcourse.par14,'score14':golfcourse.par14,'score15':golfcourse.par15,
            'score16':golfcourse.par16,'score17':golfcourse.par17,'score18':golfcourse.par18,
            'drive1':'None','longiron1':'None','approach1':'None','chip1':'None','putt1':'None',
            'drive2':'None','longiron2':'None','approach2':'None','chip2':'None','putt2':'None',
            'drive3':'None','longiron3':'None','approach3':'None','chip3':'None','putt3':'None',
            'drive4':'None','longiron4':'None','approach4':'None','chip4':'None','putt4':'None',
            'drive5':'None','longiron5':'None','approach5':'None','chip5':'None','putt5':'None',
            'drive6':'None','longiron6':'None','approach6':'None','chip6':'None','putt6':'None',
            'drive7':'None','longiron7':'None','approach7':'None','chip7':'None','putt7':'None',
            'drive8':'None','longiron8':'None','approach8':'None','chip8':'None','putt8':'None',
            'drive9':'None','longiron9':'None','approach9':'None','chip9':'None','putt9':'None',
            'drive10':'None','longiron10':'None','approach10':'None','chip10':'None','putt10':'None',
            'drive11':'None','longiron11':'None','approach11':'None','chip11':'None','putt11':'None',
            'drive12':'None','longiron12':'None','approach12':'None','chip12':'None','putt12':'None',
            'drive13':'None','longiron13':'None','approach13':'None','chip13':'None','putt13':'None',
            'drive14':'None','longiron14':'None','approach14':'None','chip14':'None','putt14':'None',
            'drive15':'None','longiron15':'None','approach15':'None','chip15':'None','putt15':'None',
            'drive16':'None','longiron16':'None','approach16':'None','chip16':'None','putt16':'None',
            'drive17':'None','longiron17':'None','approach17':'None','chip17':'None','putt17':'None',
            'drive18':'None','longiron18':'None','approach18':'None','chip18':'None','putt18':'None',
        })
    return render(request, 'golfscores/scoresave.html', {
        'form': form, 'coursedata': coursedata
    })

@login_required
def golfscore_detail(request, pk):
    golfscores = get_object_or_404(Golfscore, pk=pk)
    golfcourse = GolfCourses.objects.filter(course=golfscores.course)
    totalscores = get_object_or_404(TotalScores, pk=pk)
    shotpercentages = get_object_or_404(ShotPercentages, pk=pk)
    return render(request, 'golfscores/golfscore_detail.html', {
        'golfscores': golfscores, 'golfcourse': golfcourse, 'totalscores': totalscores, 'shotpercentages': shotpercentages
    })

@login_required
def golfscore_edit(request, pk):
    user = User.objects.all()
    golfscores = get_object_or_404(Golfscore, pk=pk)
    golfcourse = golfscores.course
    coursedata = GolfCourses.objects.filter(course=golfcourse)
    if request.method == "POST":
        form = PostForm(request.POST, instance=golfscores)
        if form.is_valid():
            golfscores = form.save(commit=False)
            golfscores.save()
            x = get_object_or_404(Golfscore, pk=pk)
            y = GolfCourses.objects.get(course=x.course)
            drivearray = [x.drive1, x.drive2, x.drive3, x.drive4, x.drive5, x.drive6, x.drive7, x.drive8, x.drive9, x.drive10, x.drive11, x.drive12, x.drive13, x.drive14, x.drive15, x.drive16, x.drive17, x.drive18]
            longironarray = [x.longiron1, x.longiron2, x.longiron3, x.longiron4, x.longiron5, x.longiron6, x.longiron7, x.longiron8, x.longiron9, x.longiron10, x.longiron11, x.longiron12, x.longiron13, x.longiron14, x.longiron15, x.longiron16, x.longiron17, x.longiron18]
            approacharray = [x.approach1, x.approach2, x.approach3, x.approach4, x.approach5, x.approach6, x.approach7, x.approach8, x.approach9, x.approach10, x.approach11, x.approach12, x.approach13, x.approach14, x.approach15, x.approach16, x.approach17, x.approach18]
            chiparray = [x.chip1, x.chip2, x.chip3, x.chip4, x.chip5, x.chip6, x.chip7, x.chip8, x.chip9, x.chip10, x.chip11, x.chip12, x.chip13, x.chip14, x.chip15, x.chip16, x.chip17, x.chip18]
            puttarray = [x.putt1, x.putt2, x.putt3, x.putt4, x.putt5, x.putt6, x.putt7, x.putt8, x.putt9, x.putt10, x.putt11, x.putt12, x.putt13, x.putt14, x.putt15, x.putt16, x.putt17, x.putt18]
            courseoutwards = sum([y.par1, y.par2, y.par3, y.par4, y.par5, y.par6, y.par7, y.par8, y.par9])
            courseinwards = sum([y.par10, y.par11, y.par12, y.par13, y.par14, y.par15, y.par16, y.par17, y.par18])
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
            r = ShotPercentages(author = x.author, drivepercentage = sumvalues1, longironpercentage = sumvalues2, approachpercentage = sumvalues3, chippercentage = sumvalues4, puttpercentage = sumvalues5, course = x.course, pk=x.pk)
            s = TotalScores(author = x.author, courseoutwards = courseoutwards, courseinwards = courseinwards, coursepar = coursepar, scoreoutwards = scoreoutwards, scoreinwards = scoreinwards, scoretotal = scoretotal, overunderpar = overunderpar, course = x.course, pk=x.pk)
            r.save()
            s.save()
            return redirect('golfscore_detail', pk=golfscores.pk)
    else:
        form = PostForm(instance=golfscores)
    return render(request, 'golfscores/golfscore_edit.html', {
        'form': form, 'coursedata': coursedata
    })

def golfscore_remove(request, pk):
    golfscore = get_object_or_404(Golfscore, pk=pk)
    totalscores = get_object_or_404(TotalScores, pk=pk)
    shotpercentages = get_object_or_404(ShotPercentages, pk=pk)
    golfscore.delete()
    totalscores.delete()
    shotpercentages.delete()
    return redirect('display')

def plot(request, chartID = 'chart_ID', chart_type = 'column', chart_height = 500):
    current_user = request.user
    fill = ShotPercentages.objects.filter(author_id=request.user).order_by('-pk')[:5]
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
    title = {"text": 'Good Shot Percentages: Average for last 5 rounds'}
    xAxis = {"title": {"text": 'Shot Type'}, "categories": ['Drive', 'Longiron', 'Approach', 'Chip', 'Putt']}
    yAxis = {"title": {"text": 'Percentages (%)'}}
    series = [{"name": 'Average Good Shot Percentage', "colorByPoint": 'true', "data": [DR, LI, AP, CH, PU]}]

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

def plot3(request, chartID = 'chart_ID', chartID2 = 'chart_ID2', chartID3 = 'chart_ID3', chart_type = 'column', chart_type2 = 'line', chart_type3 = 'column', chart_height = 500):
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
    title = {"text": 'Good Shot Percentages: All Time'}
    xAxis = {"title": {"text": 'Shot Type'}, "categories": ['Drive', 'Longiron', 'Approach', 'Chip', 'Putt']}
    yAxis = {"title": {"text": 'Percentages (%)'}}
    series = [{"name": 'Average Good Shot Percentage', "colorByPoint": 'true', "data": [DR, LI, AP, CH, PU]}]

    fill = TotalScores.objects.filter(author_id=request.user)
    OUP = list(fill.values_list('overunderpar', flat=True))

    chart2 = {"renderTo": chartID2, "type": chart_type2, "height": chart_height,}
    title2 = {"text": 'Scores Over Time'}
    xAxis2 = {"title": {"text": 'Golfrounds'}, "categories": []}
    yAxis2 = {"title": {"text": 'Shots over par'}}
    series2 = [{"name": 'Scores', "data": OUP}]

    fill = ShotPercentages.objects.filter(author_id=request.user).order_by('-pk')[:3]
    DR3 = fill.aggregate(Avg('drivepercentage'))
    DR3 = DR3['drivepercentage__avg']
    LI3 = fill.aggregate(Avg('longironpercentage'))
    LI3 = LI3['longironpercentage__avg']
    AP3 = fill.aggregate(Avg('approachpercentage'))
    AP3 = AP3['approachpercentage__avg']
    CH3 = fill.aggregate(Avg('chippercentage'))
    CH3 = CH3['chippercentage__avg']
    PU3 = fill.aggregate(Avg('puttpercentage'))
    PU3 = PU3['puttpercentage__avg']

    chart3 = {"renderTo": chartID3, "type": chart_type3, "height": chart_height,}
    title3 = {"text": 'Good Shot Percentages: Last 3 Rounds'}
    xAxis3 = {"title": {"text": 'Shot Type'}, "categories": ['Drive', 'Longiron', 'Approach', 'Chip', 'Putt']}
    yAxis3 = {"title": {"text": 'Percentages (%)'}}
    series3 = [{"name": 'Average Good Shot Percentage', "colorByPoint": 'true', "data": [DR3, LI3, AP3, CH3, PU3]}]


    return render(request, 'golfscores/Chart3.html', {'chartID': chartID, 'chart': chart,
                                                    'series': series, 'title': title,
                                                    'xAxis': xAxis, 'yAxis': yAxis, 'current_user': current_user,
                                                    'chartID2': chartID2, 'chart2': chart2,
                                                    'series2': series2, 'title2': title2,
                                                    'xAxis2': xAxis2, 'yAxis2': yAxis2,
                                                    'chartID3': chartID3, 'chart3': chart3,
                                                    'series3': series3, 'title3': title3,
                                                    'xAxis3': xAxis3, 'yAxis3': yAxis3,})

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
