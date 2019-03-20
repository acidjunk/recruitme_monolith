from django.shortcuts import render_to_response
from django.template.context import RequestContext

def test(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('social_login/test.html',
                             context_instance=context)