from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout

def login(request):
    # context = RequestContext(request, {
    #     'request': request, 'user': request.user})
    # return render_to_response('login.html', context_instance=context)
    return render(request, 'accounts/login.html')

def logout(request):
    auth_logout(request)
    return redirect('/')


