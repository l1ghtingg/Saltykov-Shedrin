from django.shortcuts import render
from django.urls import reverse

def mainpage(request):
    context = {
        'prev_page': None,
        'next_page': None,
        'is_mainpage': True
    }
    return render(request, 'mainpage.html', context)


def biography(request):
    context = {
        'prev_page': reverse('mainpage'),
        'next_page': reverse('housepage')
    }
    return render(request, 'biography.html', context)

def housepage(request):
    context = {
        'prev_page': reverse('biography'),
        'next_page': reverse('meeting')
    }
    return render(request, 'housepage.html', context)

def meeting(request):
    context = {
        'prev_page': reverse('housepage'),
        'next_page': reverse('employment')
    }
    return render(request, 'meeting.html', context)

def employment(request):
    context = {
        'prev_page': reverse('meeting'),
        'next_page': reverse('tr_department')
    }
    return render(request, 'employment.html', context)

def tr_department(request):
    context = {
        'prev_page': reverse('employment'),
        'next_page': reverse('hludovskoe')
    }
    return render(request, 'tr_department.html', context)

def hludovskoe(request):
    context = {
        'prev_page': reverse('tr_department'),
        'next_page': reverse('kislinskaya')
    }
    return render(request, 'hludovskoe.html', context)

def kislinskaya(request):
    context = {
        'prev_page': reverse('hludovskoe'),
        'next_page': reverse('communitywork')
    }
    return render(request, 'kislinskaya.html', context)

def communitywork(request):
    context = {
        'prev_page': reverse('kislinskaya'),
        'next_page': reverse('materials')
    }
    return render(request, 'communitywork.html', context)

def materials(request):
    context = {
        'prev_page': reverse('communitywork'),
        'next_page': None  
    }
    return render(request, 'materials.html', context)
