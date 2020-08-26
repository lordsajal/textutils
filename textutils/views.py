# my website - swajal
from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#  return HttpResponse('''<h1>personal Navigator<h1>
# <li>
# <li><a href="https://www.youtube.com">youtube</a></li>
# </ul>''')


# def about(request):
#   return HttpResponse("about helloo")


# def read(request):
#   file = open("textutils/1.txt", 'r')
#  return HttpResponse(file.read())


def index(request):
    params = {'name': 'harry', 'place': 'usa'}
    return render(request, 'index.html', params)
    # return HttpResponse("home")


def analyze(request):
    # get the text

    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == 'on':
        analyzed = ""
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'remove punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if fullcaps == 'on':
        analyzed = ""
        analyzed = djtext.upper()
        params = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char
        params = {'purpose': 'remove new lines', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed += char
        params = {'purpose': 'remove extra spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if charcount == "on":
        analyzed = ""
        k=0
        for char in djtext:
            if char != " ":
                k+=1
        analyzed = k
        params = {'purpose': 'character counting', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if removepunc != 'on' and fullcaps != 'on' and newlineremover != "on" and charcount != "on" and extraspaceremover != "on":
        return HttpResponse("error")



    return render(request, 'analyze.html', params)

# def capFirst(request):
#     return HttpResponse("capital first")
#
#
# def newLineRemove(request):
#     return HttpResponse("Line Remove")
#
#
# def spaceRemover(request):
#     return HttpResponse("remove spacee")
#
#
# def charcount(request):
#     return HttpResponse("char count")
