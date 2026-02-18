from django.shortcuts import render

def mainpage(request):
    return render(request, 'mainpage.html')
def biography(request):
    return render(request, 'biography.html')
def communitywork(request):
    return render(request, 'communitywork.html')
def employment(request):
    return render(request, 'employment.html')
def materials(request):
    return render(request, 'materials.html')