from django.shortcuts import render


def products(request):
    links_menu = [
        {'href': '', 'name': 'все'},
        {'href': '', 'name': 'дом'},
        {'href': '', 'name': 'офис'},
        {'href': '', 'name': 'модерн'},
        {'href': '', 'name': 'классика'},
    ]
    context = {
        'links_menu': links_menu
    }

    return render(request, 'mainapp/products.html', context=context)
