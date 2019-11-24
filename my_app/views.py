from django.shortcuts import render
from .models import Todo


# Create your views here.
def home(request):
    return render(request, 'base.html')


def add_item(request):
    return render(request, 'my_app/add.html')


def list_page(request):
    print(request.POST)
    if request.POST.get("add_item"):
        Todo.objects.create(text=request.POST.get("add_item"))
    elif request.POST.get("action"):
        Todo.objects.filter(id=int(request.POST.get("action"))).delete()

    stuff_for_frontend = {
        'final_postings': Todo.objects.all().values_list('id','text')
    }
    return render(request, 'my_app/list_page.html', stuff_for_frontend)
