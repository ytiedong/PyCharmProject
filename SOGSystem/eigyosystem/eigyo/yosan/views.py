from django.shortcuts import render


def yosan(request):
    return render(request, 'yosan/yosan.html', {'sales': 'c1'})