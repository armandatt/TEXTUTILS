from os import error
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request , 'index.html')

def about(request):
    return render(request , 'about.html')

def contact(request):
    return render(request , 'contact.html')

def analyze(request):
    text = request.POST.get('text' , 'default')
    checkbox = request.POST.get('removepunc', 'off')
    fullanalyzed = request.POST.get('fullcaps' , 'off')
    lineremove = request.POST.get('newlineremover' , 'off')
    puctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    newline = "\n\r"
    if checkbox == "on":
        analyzed = ""
        for char in text:
            if char not in puctuations:
                analyzed = analyzed + char
        params = {'analyzed' : analyzed}
        return render(request , 'remove_punc.html', params)
    if(fullanalyzed == 'on'):
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()
        params = {'analyzed': analyzed}
        return render(request , 'remove_punc.html' , params)
    if(lineremove == 'on'):
        analyzed = ""
        for char in text:
            if char not in newline:
                analyzed = analyzed + char
        params = {'analyzed' : analyzed}
        return render(request , 'remove_punc.html', params)

    else:
        # return HttpResponse('YOU DIDNT GAVE ANY TEXT TO ANALYZE!!!!')
        if text == '':
            # return HttpResponse('YOU DIDNT GAVE ANY TEXT TO ANALYZE!!!!')
            params = {'analyzed' : 'YOU DIDNT GAVE ANY TEXT TO ANALYZE!!!!'}
            return render(request , 'remove_punc.html', params) 

        else:
            params = {'analyzed' : text}
            return render(request , 'remove_punc.html', params) 
        

            


