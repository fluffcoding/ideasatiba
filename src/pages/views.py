from django.shortcuts import render



def front_page(request):
    return render(request, 'index.html', {})


def post_page(request):
    return render(request, 'post_page.html', {})


def search_results(request):
    return render(request, 'search.html', {})