from django.shortcuts import render


def uriage(request):
    return render(request, 'uriage/uriage.html', {'sales': 'c1'})

