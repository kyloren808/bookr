from django.shortcuts import render

def index(request):
    return render(request, 'base.html')


def book_search(request):
    search_word = request.GET.get('search_word')
    return render(request, 'book-search.html', {'search_word': search_word})

