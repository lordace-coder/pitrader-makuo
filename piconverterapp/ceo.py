# ceo program

from django.shortcuts import render

def robots(request):
    return render(request, 'piconverterapp/ceo/robot.txt')

def sitemap(request):
    return render (request, 'piconverterapp/ceo/sitemap.xml', content_type='text/xml, application/xml')

def open_search(request):
    return render (request, 'piconverterapp/ceo/searchlink.xml', content_type='text.xml, application/xml')

def app_manifest(request):
    return render (request, 'piconverterapp/ceo/app.json', content_type='application/json')