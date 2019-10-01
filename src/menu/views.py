from django.shortcuts import render, get_object_or_404
from .models import Template
from django.urls import reverse
from .forms import MenuForm


def menu(request):
    templates = Template.objects.all()

    if request.method == 'GET':
        params = request.GET
        for id, value in params.items():
            if value == "on":
                template = get_object_or_404(Template, id=id)

    context = {
        'templates': templates,
    }
    return render(request, 'menu.html', context)
