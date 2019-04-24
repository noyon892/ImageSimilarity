from django.http import HttpResponse, request
from django.shortcuts import render
from django.template import loader

from .forms import PostForm
from .models import Person, Department


def index(request):
    template = loader.get_template('index.html')
    context = {
        'departments': Department.objects.all()
    }
    return HttpResponse(template.render(context, request))


def person(request, user_id):
    template = loader.get_template('person.html')
    try:
        p = Person.objects.get(id=user_id)
    except Person.DoesNotExist:
        p = None

    context = {
        'person': p
    }
    return HttpResponse(template.render(context, request))


def person_create(request):
    template = 'person_create.html'

    if request.method == "POST":
        person_details = PostForm(request.POST, request.FILES)

        if person_details.is_valid():
            persons = person_details.save(commit=False)
            persons.save()
            context = {
                'message': "Data Submitted Successfully"
            }
            return render(request, template, context)
        else:
            return render(request, template, {'form': person_details})
    else:
        # If request.method == 'Get'
        form = PostForm(None)
        return render(request, template, {'form': form})