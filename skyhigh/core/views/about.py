from django.shortcuts import render

def about_page(request):
    return render(request, 'core/about.html')
