from django import template

register = template.Library()

@register.simple_tag
def drive(value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18):
    x = ([value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18])
    y = x.count(True)
    z = x.count(False)
    if y or z is not 0:
        sumvalues = (y/(y+z))*100
    else:
        sumvalues = 0
    sumvalues = round(sumvalues, 1)
    return sumvalues

@register.simple_tag
def longiron(value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18):
    x = ([value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18])
    y = x.count(True)
    z = x.count(False)
    if y or z is not 0:
        sumvalues = (y/(y+z))*100
    else:
        sumvalues = 0
    sumvalues = round(sumvalues, 1)
    return sumvalues

@register.simple_tag
def approach(value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18):
    x = ([value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18])
    y = x.count(True)
    z = x.count(False)
    if y or z is not 0:
        sumvalues = (y/(y+z))*100
    else:
        sumvalues = 0
    sumvalues = round(sumvalues, 1)
    return sumvalues

@register.simple_tag
def chip(value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18):
    x = ([value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18])
    y = x.count(True)
    z = x.count(False)
    if y or z is not 0:
        sumvalues = (y/(y+z))*100
    else:
        sumvalues = 0
    sumvalues = round(sumvalues, 1)
    return sumvalues

@register.simple_tag
def putt(value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18):
    x = ([value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18])
    y = x.count(True)
    z = x.count(False)
    if y or z is not 0:
        sumvalues = (y/(y+z))*100
    else:
        sumvalues = 0
    sumvalues = round(sumvalues, 1)
    return sumvalues

@register.assignment_tag
def partotals(value1, value2, value3, value4, value5, value6, value7, value8, value9,
value10, value11, value12, value13, value14, value15, value16, value17, value18,
value19, value20, value21, value22, value23, value24, value25, value26, value27,
value28, value29, value30, value31, value32, value33, value34, value35, value36):
    x = ([value1, value2, value3, value4, value5, value6, value7, value8, value9])
    courseoutwards = sum(x)
    y = ([value10, value11, value12, value13, value14, value15, value16, value17, value18])
    courseinwards = sum(y)
    z = ([value19, value20, value21, value22, value23, value24, value25, value26, value27])
    scoreoutwards = sum(z)
    w = ([value28, value29, value30, value31, value32, value33, value34, value35, value36])
    scoreinwards = sum(w)
    coursepar = courseoutwards + courseinwards
    scoretotal = scoreoutwards + scoreinwards
    overunderpar = scoretotal - coursepar
    outputarray = [courseoutwards, courseinwards, coursepar, scoreoutwards, scoreinwards, scoretotal, overunderpar]
    return outputarray
