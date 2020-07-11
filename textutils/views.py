# this file is not default django file.
from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     return HttpResponse('''<h1> Hello Raj </h1> <a href="https://www.speedtest.net/"> Speed test</a>''')

# def about(request):
#     return HttpResponse("about Hello Raj")

def index(request):

    return render(request, 'index.html')

    # return HttpResponse('''<h1> Home </h1> </br><a href="http://127.0.0.1:8000/removepunc"> remove punc</a>&nbsp; <a href="http://127.0.0.1:8000/capfirst"> caiptalize first</a>&nbsp; <a href="http://127.0.0.1:8000/newlineremove"> new line remove</a>&nbsp; <a href="http://127.0.0.1:8000/spaceremove"> space remove</a>&nbsp; ''')


def analyze(request):

    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    if removepunc == "on":
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Punctuations Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = djtext.upper()
        djtext = analyzed
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}

    if newlineremover == 'on':
        djtext1 = djtext.split('\n')
        djtext1 = ' '.join(djtext1)
        analyzed = ""
        for char in djtext1:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        djtext = analyzed
        params = {'purpose': 'New line removed', 'analyzed_text': analyzed}

    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char
        djtext = analyzed
        params = {'purpose': 'Extra space removed', 'analyzed_text': analyzed}

    if charcounter == 'on':
        analyzed1 = ""

        for index, char in enumerate(djtext):
            if not (djtext[index] == ' ' or (djtext[index] == '\n' or djtext[index] == '\r')):
                analyzed1 = analyzed1 + char
        totalchar = len(analyzed1)

        if extraspaceremover == 'on' or newlineremover == 'on' or removepunc == 'on' or fullcaps == 'on':
            params = {'purpose': 'Characters count', 'analyzed_text': (
                f'Total characters: {totalchar}\n{analyzed}')}
        else:

            params = {'purpose': 'Characters count', 'analyzed_text': (
                f'Total characters: {totalchar}\n{analyzed1}')}

    if extraspaceremover == 'on' or newlineremover == 'on' or removepunc == 'on' or fullcaps == 'on' or charcounter == 'on':
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error - Please select at least one solution and try again.")
