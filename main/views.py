from django.shortcuts import render
from django.conf import settings

def get_common_context():
    return {
        'bank_name': settings.DATA['BANK_NAME']
    }

def index(request):
    context = get_common_context()
    return render(request, 'main/index.html', context)

def why(request):
    context = get_common_context()
    context['why']=settings.DATA['WHY']
    return render(request, 'main/why.html', context)

def help(request):
    context = get_common_context()
    context['help']=settings.DATA['HELP']
    return render(request, 'main/help.html', context)

def careers(request):
    context = get_common_context()
    return render(request, 'main/careers.html', context)

def about_us(request):
    context = get_common_context()
    context['about_us'] = settings.DATA['ABOUT_US']
    return render(request, 'main/about_us.html', context)
