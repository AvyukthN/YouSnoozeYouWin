from django.shortcuts import render
from coderageapp.drowsiness import predictor

# Create your views here.
def home(request):
    sleepybool = predictor()
    if sleepybool:
        out = "SLEEPY"
    else:
        out = "NOT SLEEPY"
    context = {"issleepy": out, "issleepybool": sleepybool}
    return render(request, 'home.html', context)