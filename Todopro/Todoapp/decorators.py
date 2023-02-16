from django.shortcuts import redirect


def login_required(function):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return function(request,*args,**kwargs)
        else:
            return redirect('login')
    return wrapper