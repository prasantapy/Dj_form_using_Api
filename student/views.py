from django.shortcuts import render
from.forms import StudentRegistration
# Create your views here.
def showformdata(req):
    fm=StudentRegistration()
    return render(req,'student/index.html',
    {'form':fm})
