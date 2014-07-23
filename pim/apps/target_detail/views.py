from django.shortcuts import render
from django.core.context_processors import csrf
import configs as CONFIG

# Create your views here.
def index(request):
    print 'target_detail'    
    main_url = CONFIG.TOP_URL
    main_content = CONFIG.TARGET_DETAIL_MAIN_URL
    sub_content = CONFIG.TARGET_DETAIL_SUB_URL
    c = {}    
    url_dict = {'main_url':main_url, 
                'main_content':main_content,
                'sub_content':sub_content}
    c.update(csrf(request))
    c.update(url_dict)
    return render(request, 'common/main.html', c)