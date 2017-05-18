from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.core import urlresolvers

def index_display(request):
    return render(request, 'accounts/index.html')

def user_login(request):
    postdata = request.POST.copy()
    username = postdata.get('username', '')
    password = postdata.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        url = urlresolvers.reverse('products:product_details')
        return HttpResponseRedirect(url)
    else:
        error_msg = "Incorrect username or password. Please try again"
        return render(request, 'accounts/index.html', locals())


def logout_user(request):
    logout(request)
    url = urlresolvers.reverse('accounts:index_display')
    return HttpResponseRedirect(url)








































































