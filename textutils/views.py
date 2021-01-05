# I have created this file - DS
from django.http import HttpResponse
from django.shortcuts import render
import string
# Personal Navigator
# def index(request):
#     html_code = '''<a href = "http://www.google.com" > Google </a> &emsp;
#     <a href = "http://www.linkedin.com" > LinkedIn </a>&emsp;
#     <a href = "http://www.instagram.com" > Instagram </a>&emsp;
#     <a href = "http://www.reddit.com" > Reddit </a>&emsp;
#     <a href = "http://www.youtube.com" > Youtube </a>&emsp;
#     '''
#     return HttpResponse(html_code)


def index(request):
    #params = {'name': 'DS', 'location': 'Earth'}
    return render(request, 'index.html')
   # return HttpResponse('<h1>Harry</h1>')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # print(djtext)
    print(newlineremover+"= New line remover flag")
    # print(removepunc)
    # print(fullcaps)
    char_count = {}
    analyzed = djtext
    if removepunc == "on":
        analyzed = "".join(
            [i for i in analyzed if i not in string.punctuation])
        #analyzed = djtext
        params = {'purpose': 'Remove Punctuations',
                  'analyzed_text': analyzed, 'char_count': char_count}
        # return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = analyzed.upper()
        params = {'purpose': 'Full Capitals',
                  'analyzed_text': analyzed, "char_count": char_count}

    if newlineremover == "on":
        analyzed = analyzed.replace('\n', '').replace('\r', '')
        # print(analyzed1)
        params = {'purpose': 'New Line Removed',
                  'analyzed_text': analyzed, "char_count": char_count}

    if extraspaceremover == "on":
        analyzed = " ".join(analyzed.split())
        params = {'purpose': 'Extra Space Removed',
                  'analyzed_text': analyzed, "char_count": char_count}
    # else:
    if charcount == "on":
        for i in analyzed:
            print(i)
            if i in char_count:
                char_count[i] += 1
            else:
                char_count[i] = 1
        char_count = dict(
            sorted(char_count.items(), key=lambda item: item[1], reverse=True))
        params = {'purpose': 'Char Counted',
                  'analyzed_text': analyzed, "char_count": char_count}

    if removepunc == 'off' and fullcaps == 'off' and newlineremover == "off" and extraspaceremover == "off" and charcount == "off":
        return HttpResponse('Error')

    return render(request, 'analyze.html', params)

# def removepunc(request):
#     #Get the text#####
#     #print(request.GET.get('text', 'default'))
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     return HttpResponse('<h1>remove punc</h1>')


# def capfirst(request):
#     return HttpResponse('<h1>capitalize first</h1>')


# def newlineremove(request):
#     return HttpResponse('<h1>new line remove</h1>')


# def spaceremove(request):
#     return HttpResponse('<h1>space remove</h1>')


# def charcount(request):
#     return HttpResponse('<h1>char count</h1>')
