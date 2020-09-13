from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request,'index.html')

def index1(request):
    return render(request, 'index1.html')

def about(request):
    gettext=request.POST.get('text','defalut')
    removepunc=request.POST.get('removepunc','off')
    upper=request.POST.get('upper','off')
    print(gettext)

    punc='''!()-[]{};:'"/,`.|<>?!@#$%^&*~'''
    if(removepunc=='on'):
        analyzed=""
        for char in gettext:
            if char not in punc:
                analyzed= analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        gettext=analyzed
        
    
    if (upper=="on"):
        analyzed=""
        for char in gettext:
            analyzed=analyzed+char.upper()
       
        params={'purpose':'Cpitalize all text','analyzed_text':analyzed}
        gettext=analyzed

    
    if (upper=='off' and removepunc=='off'):
        return HttpResponse("Please select any option Behnchod")

    return render(request,'about.html',params)

def contact(request):
    print(request.GET.get('text','defalut'))
    return HttpResponse("<a href='/'>Home</a><h1>Hello Connections</h1>")


def services(request):
    return HttpResponse('I am in service Call me later <a href="about">About</a>')


