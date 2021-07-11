from django.shortcuts import render
import random

# Create your views here.
from django.http import HttpResponse as hp

def home(request):
    return render(request, 'generator/home.html',)
def password(request):
    pas = ''
    lenth = int(request.GET.get('length', 8))

    chars = list('abcdefghijklmnopqrstwxyzertgyhnjmk')
    if request.GET.get('upercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRWTGXWZ'))
    if request.GET.get('number'):
        chars.extend(list('123456789083735210362527'))
    if request.GET.get('special'):
        chars.extend(list('!@#$%^&*#*^#&$%'))

    for i in range(lenth):
        pas += random.choice(chars)
    return render(request, 'generator/password.html',{"password":pas} )

def meh(request):
    return render(request , 'generator/meh.html')


