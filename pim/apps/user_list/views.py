from django.shortcuts import render
from django.core.context_processors import csrf
import configs as CONFIG

# Create your views here.
def index(request):
    print 'user_list'    
    main_url = CONFIG.TOP_URL
    page_title = CONFIG.USER_LIST_PAGE_TITLE_URL
    main_content = CONFIG.USER_LIST_MAIN_URL
    sub_content = CONFIG.USER_LIST_SUB_URL
    action_dict = CONFIG.ACTION_DICT
    c = {}    
    url_dict = {'main_url':main_url, 
                'page_title':page_title, 
                'main_content':main_content,
                'sub_content':sub_content}
    c.update(csrf(request))
    c.update(url_dict)
    c.update(action_dict)
    return render(request, 'common/main.html', c)