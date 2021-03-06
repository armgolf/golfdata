from django import forms
from django.forms import ModelForm, NumberInput, ModelChoiceField, RadioSelect
from .models import Golfscore, GolfCourses, Signup
from django.utils.safestring import mark_safe

class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class PostForm(forms.ModelForm):

    class Meta:
        model = Golfscore
        fields = ('score1','drive1', 'longiron1', 'approach1', 'chip1', 'putt1',
         'score2','drive2', 'longiron2', 'approach2', 'chip2', 'putt2',
         'score3','drive3', 'longiron3', 'approach3', 'chip3', 'putt3',
         'score4','drive4', 'longiron4', 'approach4', 'chip4', 'putt4',
         'score5','drive5', 'longiron5', 'approach5', 'chip5', 'putt5',
         'score6','drive6', 'longiron6', 'approach6', 'chip6', 'putt6',
         'score7','drive7', 'longiron7', 'approach7', 'chip7', 'putt7',
         'score8','drive8', 'longiron8', 'approach8', 'chip8', 'putt8',
         'score9','drive9', 'longiron9', 'approach9', 'chip9', 'putt9',
         'score10','drive10', 'longiron10', 'approach10', 'chip10', 'putt10',
         'score11','drive11', 'longiron11', 'approach11', 'chip11', 'putt11',
         'score12','drive12', 'longiron12', 'approach12', 'chip12', 'putt12',
         'score13','drive13', 'longiron13', 'approach13', 'chip13', 'putt13',
         'score14','drive14', 'longiron14', 'approach14', 'chip14', 'putt14',
         'score15','drive15', 'longiron15', 'approach15', 'chip15', 'putt15',
         'score16','drive16', 'longiron16', 'approach16', 'chip16', 'putt16',
         'score17','drive17', 'longiron17', 'approach17', 'chip17', 'putt17',
         'score18','drive18', 'longiron18', 'approach18', 'chip18', 'putt18',
         'opponent1', 'opponent2', 'opponent3', 'o1totalscore', 'o2totalscore', 'o3totalscore',
         )
        widgets = {
            'score1': NumberInput(attrs={'class': 'classybox'}),
            'score2': NumberInput(attrs={'class': 'classybox'}),
            'score3': NumberInput(attrs={'class': 'classybox'}),
            'score4': NumberInput(attrs={'class': 'classybox'}),
            'score5': NumberInput(attrs={'class': 'classybox'}),
            'score6': NumberInput(attrs={'class': 'classybox'}),
            'score7': NumberInput(attrs={'class': 'classybox'}),
            'score8': NumberInput(attrs={'class': 'classybox'}),
            'score9': NumberInput(attrs={'class': 'classybox'}),
            'score10': NumberInput(attrs={'class': 'classybox'}),
            'score11': NumberInput(attrs={'class': 'classybox'}),
            'score12': NumberInput(attrs={'class': 'classybox'}),
            'score13': NumberInput(attrs={'class': 'classybox'}),
            'score14': NumberInput(attrs={'class': 'classybox'}),
            'score15': NumberInput(attrs={'class': 'classybox'}),
            'score16': NumberInput(attrs={'class': 'classybox'}),
            'score17': NumberInput(attrs={'class': 'classybox'}),
            'score18': NumberInput(attrs={'class': 'classybox'}),
            'o1totalscore': NumberInput(attrs={'class': 'classybox'}),
            'o2totalscore': NumberInput(attrs={'class': 'classybox'}),
            'o3totalscore': NumberInput(attrs={'class': 'classybox'}),
            'drive1': RadioSelect(renderer=HorizontalRadioRenderer),
            'longiron1': RadioSelect(renderer=HorizontalRadioRenderer),
            'approach1': RadioSelect(renderer=HorizontalRadioRenderer),
            'chip1': RadioSelect(renderer=HorizontalRadioRenderer),
            'putt1': RadioSelect(renderer=HorizontalRadioRenderer),
            'drive2': RadioSelect(renderer=HorizontalRadioRenderer),
            'longiron2': RadioSelect(renderer=HorizontalRadioRenderer),
            'approach2': RadioSelect(renderer=HorizontalRadioRenderer),
            'chip2': RadioSelect(renderer=HorizontalRadioRenderer),
            'putt2': RadioSelect(renderer=HorizontalRadioRenderer),
            'drive3': RadioSelect(renderer=HorizontalRadioRenderer),
            'longiron3': RadioSelect(renderer=HorizontalRadioRenderer),
            'approach3': RadioSelect(renderer=HorizontalRadioRenderer),
            'chip3': RadioSelect(renderer=HorizontalRadioRenderer),
            'putt3': RadioSelect(renderer=HorizontalRadioRenderer),
            'drive4': RadioSelect(renderer=HorizontalRadioRenderer),
            'longiron4': RadioSelect(renderer=HorizontalRadioRenderer),
            'approach4': RadioSelect(renderer=HorizontalRadioRenderer),
            'chip4': RadioSelect(renderer=HorizontalRadioRenderer),
            'putt4': RadioSelect(renderer=HorizontalRadioRenderer),
            'drive5': RadioSelect(renderer=HorizontalRadioRenderer),
            'longiron5': RadioSelect(renderer=HorizontalRadioRenderer),
            'approach5': RadioSelect(renderer=HorizontalRadioRenderer),
            'chip5': RadioSelect(renderer=HorizontalRadioRenderer),
            'putt5': RadioSelect(renderer=HorizontalRadioRenderer),
            'drive6': RadioSelect(renderer=HorizontalRadioRenderer),
            'longiron6': RadioSelect(renderer=HorizontalRadioRenderer),
            'approach6': RadioSelect(renderer=HorizontalRadioRenderer),
            'chip6': RadioSelect(renderer=HorizontalRadioRenderer),
            'putt6': RadioSelect(renderer=HorizontalRadioRenderer),
            'drive7': RadioSelect(renderer=HorizontalRadioRenderer),
            'longiron7': RadioSelect(renderer=HorizontalRadioRenderer),
            'approach7': RadioSelect(renderer=HorizontalRadioRenderer),
            'chip7': RadioSelect(renderer=HorizontalRadioRenderer),
            'putt7': RadioSelect(renderer=HorizontalRadioRenderer),
            'drive8': RadioSelect(renderer=HorizontalRadioRenderer),
            'longiron8': RadioSelect(renderer=HorizontalRadioRenderer),
            'approach8': RadioSelect(renderer=HorizontalRadioRenderer),
            'chip8': RadioSelect(renderer=HorizontalRadioRenderer),
            'putt8': RadioSelect(renderer=HorizontalRadioRenderer),
            'drive9': RadioSelect(renderer=HorizontalRadioRenderer),
            'longiron9': RadioSelect(renderer=HorizontalRadioRenderer),
            'approach9': RadioSelect(renderer=HorizontalRadioRenderer),
            'chip9': RadioSelect(renderer=HorizontalRadioRenderer),
            'putt9': RadioSelect(renderer=HorizontalRadioRenderer),
            'drive10': RadioSelect(renderer=HorizontalRadioRenderer),
            'longiron10': RadioSelect(renderer=HorizontalRadioRenderer),
            'approach10': RadioSelect(renderer=HorizontalRadioRenderer),
            'chip10': RadioSelect(renderer=HorizontalRadioRenderer),
            'putt10': RadioSelect(renderer=HorizontalRadioRenderer),
            'drive11': RadioSelect(renderer=HorizontalRadioRenderer),
            'longiron11': RadioSelect(renderer=HorizontalRadioRenderer),
            'approach11': RadioSelect(renderer=HorizontalRadioRenderer),
            'chip11': RadioSelect(renderer=HorizontalRadioRenderer),
            'putt11': RadioSelect(renderer=HorizontalRadioRenderer),
            'drive12': RadioSelect(renderer=HorizontalRadioRenderer),
            'longiron12': RadioSelect(renderer=HorizontalRadioRenderer),
            'approach12': RadioSelect(renderer=HorizontalRadioRenderer),
            'chip12': RadioSelect(renderer=HorizontalRadioRenderer),
            'putt12': RadioSelect(renderer=HorizontalRadioRenderer),
            'drive13': RadioSelect(renderer=HorizontalRadioRenderer),
            'longiron13': RadioSelect(renderer=HorizontalRadioRenderer),
            'approach13': RadioSelect(renderer=HorizontalRadioRenderer),
            'chip13': RadioSelect(renderer=HorizontalRadioRenderer),
            'putt13': RadioSelect(renderer=HorizontalRadioRenderer),
            'drive14': RadioSelect(renderer=HorizontalRadioRenderer),
            'longiron14': RadioSelect(renderer=HorizontalRadioRenderer),
            'approach14': RadioSelect(renderer=HorizontalRadioRenderer),
            'chip14': RadioSelect(renderer=HorizontalRadioRenderer),
            'putt14': RadioSelect(renderer=HorizontalRadioRenderer),
            'drive15': RadioSelect(renderer=HorizontalRadioRenderer),
            'longiron15': RadioSelect(renderer=HorizontalRadioRenderer),
            'approach15': RadioSelect(renderer=HorizontalRadioRenderer),
            'chip15': RadioSelect(renderer=HorizontalRadioRenderer),
            'putt15': RadioSelect(renderer=HorizontalRadioRenderer),
            'drive16': RadioSelect(renderer=HorizontalRadioRenderer),
            'longiron16': RadioSelect(renderer=HorizontalRadioRenderer),
            'approach16': RadioSelect(renderer=HorizontalRadioRenderer),
            'chip16': RadioSelect(renderer=HorizontalRadioRenderer),
            'putt16': RadioSelect(renderer=HorizontalRadioRenderer),
            'drive17': RadioSelect(renderer=HorizontalRadioRenderer),
            'longiron17': RadioSelect(renderer=HorizontalRadioRenderer),
            'approach17': RadioSelect(renderer=HorizontalRadioRenderer),
            'chip17': RadioSelect(renderer=HorizontalRadioRenderer),
            'putt17': RadioSelect(renderer=HorizontalRadioRenderer),
            'drive18': RadioSelect(renderer=HorizontalRadioRenderer),
            'longiron18': RadioSelect(renderer=HorizontalRadioRenderer),
            'approach18': RadioSelect(renderer=HorizontalRadioRenderer),
            'chip18': RadioSelect(renderer=HorizontalRadioRenderer),
            'putt18': RadioSelect(renderer=HorizontalRadioRenderer),
        }

class gcselection(forms.Form):
    field1 = ModelChoiceField(queryset=GolfCourses.objects.order_by('course'), to_field_name="course", label='Which course did you play?', empty_label="select golf course")

class PNumber(forms.ModelForm):

    class Meta:
        model = Signup
        fields = ('phonenumber',)
