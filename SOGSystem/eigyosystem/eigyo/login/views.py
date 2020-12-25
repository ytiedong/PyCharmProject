from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from eigyosystem.eigyo.login.forms import LoginForm


def logineigyo(request):
    if request.method == 'POST':

        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('eigyosystem:index'))
            else:
                return render(request, 'login/logineigyo.html',
                              {'form': form, 'message': 'Wrong password Please Try agagin'})
    else:
        form = LoginForm()

    return render(request, 'login/logineigyo.html', {'form': form})


def test(request):

    print('7777777777745564564567456456564')
    return render(request, 'test.html', {'form': 'form'})
