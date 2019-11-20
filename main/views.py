from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from . import models
from main.models import Main


# Create your views here.
def home(request):
    todo_items = Main.objects.all().order_by('-added_date')
    return render(request, 'main/index.html', {
        "todo_items": todo_items
    })


@csrf_exempt
def add_todo(request):
    added_date = timezone.now()
    content = request.POST.get('text')
    models.Main.objects.create(text=content)
    return HttpResponseRedirect('/')


@csrf_exempt
def delete_todo(request, todo_id):
    Main.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')
