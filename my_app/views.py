from django.shortcuts import render
from .models import Todo


# Create your views here.
def home(request):
    return render(request, 'base.html')


def add_item(request):
    return render(request, 'my_app/add.html')


def list_page(request):
    if request.POST.get("add_item"):
        Todo.objects.create(text=request.POST.get("add_item"))

    stuff_for_frontend = {
        'final_postings': Todo.objects.all()
    }
    return render(request, 'my_app/list_page.html', stuff_for_frontend)
