from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from eigyosystem.eigyo.menu import viewcommon


@login_required
def index(request):
    indexes = viewcommon.indexview()

    return render(request, 'menu/index.html', {'indexes': indexes})
