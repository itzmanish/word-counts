from django.shortcuts import render
from django.http import HttpResponse
import operator


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def count(request):
    yourtext = request.GET['yourtext']
    splitted_text = yourtext.split()

    worddictionary = {}

    for words in splitted_text:
        if words in worddictionary:
            worddictionary[words] += 1

        else:
            worddictionary[words] = 1

    sorted_words = sorted(worddictionary.items(),
                          key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', context={'yourtext': yourtext, 'length': len(splitted_text), 'sorted_words': sorted_words})
