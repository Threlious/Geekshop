from django.shortcuts import render


def index(request):
    context = {
        'no': 'Oh no',
        'header': True,
        'info': False
    }

    return render(request, 'geekshop/index.html', context)


def contacts(request):
    return render(request, 'geekshop/contact.html')