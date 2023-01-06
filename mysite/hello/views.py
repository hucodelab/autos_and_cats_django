from django.http import HttpResponse

# Create your views here.

# https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.HttpRequest.COOKIES
# HttpResponse.set_cookie(key, value='', max_age=None, expires=None, path='/', 
#     domain=None, secure=None, httponly=False, samesite=None)

def cookie(request):
    print(request.COOKIES)
    oldval = request.COOKIES.get('dj4e_cookie', 'b3e31e79')
    resp = HttpResponse(oldval)
    resp.set_cookie('dj4e_cookie', 'b3e31e79', max_age=1000) # seconds until expire
    
    # sessions
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits 
    if num_visits > 4 : del(request.session['num_visits'])
    resp.write('view count='+str(num_visits))
    
    return resp

# https://www.youtube.com/watch?v=Ye8mB6VsUHw