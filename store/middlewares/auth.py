from django.shortcuts import redirect

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        print(request.session.get('customer')) #shows None if not login
        returnUrl = request.META['PATH_INFO']
        print(request.META['PATH_INFO'])
        if not request.session.get('customer'): # if customer found means you are logged in
            # return redirect('login')  #important to return then only login page will be shown on going order tab without any user logged in it
            return redirect(f'login?return_url={returnUrl}')  #important to return then only login page will be shown on going order tab without any user logged in it
            
        response = get_response(request)
        return response

    return middleware