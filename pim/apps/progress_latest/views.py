from django.shortcuts import render
from django.core.context_processors import csrf
import configs as CONFIG
import services as SERVICES

# Create your views here.
def index(request):
    print 'progress_latest'
    user = request.session['user']
    main_url = CONFIG.TOP_URL
    main_content = CONFIG.PROGRESS_LATEST_MAIN_URL
    sub_content = CONFIG.PROGRESS_LATEST_SUB_URL
    c = {}
    user_dict = {'user':user}
    url_dict = {'main_url':main_url, 
                'main_content':main_content,
                'sub_content':sub_content}
    c.update(csrf(request))
    c.update(url_dict)
    c.update(user_dict)
    return render(request, 'common/main.html', c)