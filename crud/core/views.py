from django.shortcuts import render
from .models import Person
from django.http import HttpResponseRedirect

# Create your views here.
def core_index(request):
    persons = Person.objects.all()
    context = {
        'persons': persons
    }
    return render(request, 'core/index.html', context)

def core_detail(request, id):
    person = Person.objects.get(id = id)
    context = {
        'person': person
    }
    return render(request, 'core/detail.html', context)

def core_delete(request,id):
    person = Person.objects.get(id = id)
    person.delete()
    return HttpResponseRedirect('/core/')