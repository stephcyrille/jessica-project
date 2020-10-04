from django.shortcuts import render


def login(request):
    template = 'client/login.html'
    context = {}
    return render(request, template, context)
