from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

CHOICES = (
    (True, "Good"),
    (False, "Bad"),
    (None, "N/a")

)

class Golfscore(models.Model):
    course = models.CharField(max_length=200)
    holeno1 = models.IntegerField(default=1)
    par1 = models.IntegerField(default=4)
    score1 = models.IntegerField(default=4)
    drive1 = models.NullBooleanField(choices=CHOICES)
    longiron1 = models.NullBooleanField(choices=CHOICES)
    approach1 = models.NullBooleanField(choices=CHOICES)
    chip1 = models.NullBooleanField(choices=CHOICES)
    putt1 = models.NullBooleanField(choices=CHOICES)
    holeno2 = models.IntegerField(default=2)
    par2 = models.IntegerField(default=4)
    score2 = models.IntegerField(default=4)
    drive2 = models.NullBooleanField(choices=CHOICES)
    longiron2 = models.NullBooleanField(choices=CHOICES)
    approach2 = models.NullBooleanField(choices=CHOICES)
    chip2 = models.NullBooleanField(choices=CHOICES)
    putt2 = models.NullBooleanField(choices=CHOICES)
    holeno3 = models.IntegerField(default=3)
    par3 = models.IntegerField(default=4)
    score3 = models.IntegerField(default=4)
    drive3 = models.NullBooleanField(choices=CHOICES)
    longiron3 = models.NullBooleanField(choices=CHOICES)
    approach3 = models.NullBooleanField(choices=CHOICES)
    chip3 = models.NullBooleanField(choices=CHOICES)
    putt3 = models.NullBooleanField(choices=CHOICES)
    holeno4 = models.IntegerField(default=4)
    par4 = models.IntegerField(default=4)
    score4 = models.IntegerField(default=4)
    drive4 = models.NullBooleanField(choices=CHOICES)
    longiron4 = models.NullBooleanField(choices=CHOICES)
    approach4 = models.NullBooleanField(choices=CHOICES)
    chip4 = models.NullBooleanField(choices=CHOICES)
    putt4 = models.NullBooleanField(choices=CHOICES)
    holeno5 = models.IntegerField(default=5)
    par5 = models.IntegerField(default=4)
    score5 = models.IntegerField(default=4)
    drive5 = models.NullBooleanField(choices=CHOICES)
    longiron5 = models.NullBooleanField(choices=CHOICES)
    approach5 = models.NullBooleanField(choices=CHOICES)
    chip5 = models.NullBooleanField(choices=CHOICES)
    putt5 = models.NullBooleanField(choices=CHOICES)
    holeno6 = models.IntegerField(default=6)
    par6 = models.IntegerField(default=4)
    score6 = models.IntegerField(default=4)
    drive6 = models.NullBooleanField(choices=CHOICES)
    longiron6 = models.NullBooleanField(choices=CHOICES)
    approach6 = models.NullBooleanField(choices=CHOICES)
    chip6 = models.NullBooleanField(choices=CHOICES)
    putt6 = models.NullBooleanField(choices=CHOICES)
    holeno7 = models.IntegerField(default=7)
    par7 = models.IntegerField(default=4)
    score7 = models.IntegerField(default=4)
    drive7 = models.NullBooleanField(choices=CHOICES)
    longiron7 = models.NullBooleanField(choices=CHOICES)
    approach7 = models.NullBooleanField(choices=CHOICES)
    chip7 = models.NullBooleanField(choices=CHOICES)
    putt7 = models.NullBooleanField(choices=CHOICES)
    holeno8 = models.IntegerField(default=8)
    par8 = models.IntegerField(default=4)
    score8 = models.IntegerField(default=4)
    drive8 = models.NullBooleanField(choices=CHOICES)
    longiron8 = models.NullBooleanField(choices=CHOICES)
    approach8 = models.NullBooleanField(choices=CHOICES)
    chip8 = models.NullBooleanField(choices=CHOICES)
    putt8 = models.NullBooleanField(choices=CHOICES)
    holeno9 = models.IntegerField(default=9)
    par9 = models.IntegerField(default=4)
    score9 = models.IntegerField(default=4)
    drive9 = models.NullBooleanField(choices=CHOICES)
    longiron9 = models.NullBooleanField(choices=CHOICES)
    approach9 = models.NullBooleanField(choices=CHOICES)
    chip9 = models.NullBooleanField(choices=CHOICES)
    putt9 = models.NullBooleanField(choices=CHOICES)
    holeno10 = models.IntegerField(default=10)
    par10 = models.IntegerField(default=4)
    score10 = models.IntegerField(default=4)
    drive10 = models.NullBooleanField(choices=CHOICES)
    longiron10 = models.NullBooleanField(choices=CHOICES)
    approach10 = models.NullBooleanField(choices=CHOICES)
    chip10 = models.NullBooleanField(choices=CHOICES)
    putt10 = models.NullBooleanField(choices=CHOICES)
    holeno11 = models.IntegerField(default=11)
    par11 = models.IntegerField(default=4)
    score11 = models.IntegerField(default=4)
    drive11 = models.NullBooleanField(choices=CHOICES)
    longiron11 = models.NullBooleanField(choices=CHOICES)
    approach11 = models.NullBooleanField(choices=CHOICES)
    chip11 = models.NullBooleanField(choices=CHOICES)
    putt11 = models.NullBooleanField(choices=CHOICES)
    holeno12 = models.IntegerField(default=12)
    par12 = models.IntegerField(default=4)
    score12 = models.IntegerField(default=4)
    drive12 = models.NullBooleanField(choices=CHOICES)
    longiron12 = models.NullBooleanField(choices=CHOICES)
    approach12 = models.NullBooleanField(choices=CHOICES)
    chip12 = models.NullBooleanField(choices=CHOICES)
    putt12 = models.NullBooleanField(choices=CHOICES)
    holeno13 = models.IntegerField(default=13)
    par13 = models.IntegerField(default=4)
    score13 = models.IntegerField(default=4)
    drive13 = models.NullBooleanField(choices=CHOICES)
    longiron13 = models.NullBooleanField(choices=CHOICES)
    approach13 = models.NullBooleanField(choices=CHOICES)
    chip13 = models.NullBooleanField(choices=CHOICES)
    putt13 = models.NullBooleanField(choices=CHOICES)
    holeno14 = models.IntegerField(default=14)
    par14 = models.IntegerField(default=4)
    score14 = models.IntegerField(default=4)
    drive14 = models.NullBooleanField(choices=CHOICES)
    longiron14 = models.NullBooleanField(choices=CHOICES)
    approach14 = models.NullBooleanField(choices=CHOICES)
    chip14 = models.NullBooleanField(choices=CHOICES)
    putt14 = models.NullBooleanField(choices=CHOICES)
    holeno15 = models.IntegerField(default=15)
    par15 = models.IntegerField(default=4)
    score15 = models.IntegerField(default=4)
    drive15 = models.NullBooleanField(choices=CHOICES)
    longiron15 = models.NullBooleanField(choices=CHOICES)
    approach15 = models.NullBooleanField(choices=CHOICES)
    chip15 = models.NullBooleanField(choices=CHOICES)
    putt15 = models.NullBooleanField(choices=CHOICES)
    holeno16 = models.IntegerField(default=16)
    par16 = models.IntegerField(default=4)
    score16 = models.IntegerField(default=4)
    drive16 = models.NullBooleanField(choices=CHOICES)
    longiron16 = models.NullBooleanField(choices=CHOICES)
    approach16 = models.NullBooleanField(choices=CHOICES)
    chip16 = models.NullBooleanField(choices=CHOICES)
    putt16 = models.NullBooleanField(choices=CHOICES)
    holeno17 = models.IntegerField(default=17)
    par17 = models.IntegerField(default=4)
    score17 = models.IntegerField(default=4)
    drive17 = models.NullBooleanField(choices=CHOICES)
    longiron17 = models.NullBooleanField(choices=CHOICES)
    approach17 = models.NullBooleanField(choices=CHOICES)
    chip17 = models.NullBooleanField(choices=CHOICES)
    putt17 = models.NullBooleanField(choices=CHOICES)
    holeno18 = models.IntegerField(default=18)
    par18 = models.IntegerField(default=4)
    score18 = models.IntegerField(default=4)
    drive18 = models.NullBooleanField(choices=CHOICES)
    longiron18 = models.NullBooleanField(choices=CHOICES)
    approach18 = models.NullBooleanField(choices=CHOICES)
    chip18 = models.NullBooleanField(choices=CHOICES)
    putt18 = models.NullBooleanField(choices=CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    published_date = models.DateTimeField(default=timezone.now)

class ShotPercentages(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    drivepercentage = models.IntegerField(default=1)
    longironpercentage = models.IntegerField(default=1)
    approachpercentage = models.IntegerField(default=1)
    chippercentage = models.IntegerField(default=1)
    puttpercentage = models.IntegerField(default=1)

class TotalScores(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    courseoutwards = models.IntegerField(default=1)
    courseinwards = models.IntegerField(default=1)
    coursepar = models.IntegerField(default=1)
    scoreoutwards = models.IntegerField(default=1)
    scoreinwards = models.IntegerField(default=1)
    scoretotal = models.IntegerField(default=1)
    overunderpar = models.IntegerField(default=1)
