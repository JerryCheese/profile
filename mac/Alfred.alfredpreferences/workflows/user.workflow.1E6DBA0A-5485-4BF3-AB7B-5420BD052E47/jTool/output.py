import time, json, re
import native

# configs 
# candidates config
candidates_config = {
    'reg': r'(\w+)candidate$',
    'searcher': {
        'baidu': {
            'query':'https://www.baidu.com/s?ie=UTF-8&wd={query}',
            'tips': 'Searcing in Baidu with "{query}"...'
        },
        'bing': {
            'query':'https://cn.bing.com/search?q={query}',
            'tips': 'Searcing in Bing with "{query}"...'
        },
        'google': {
            'query':'https://www.baidu.com/s?ie=UTF-8&wd={query}',
            'tips': 'Searcing in Google with "{query}"...'
        },
        'taobao': {
            'query':'https://s.taobao.com/search?q={query}',
            'tips': 'Searcing in Taobao with "{query}"...'
        }
    },
    'handler': lambda res,tpl: re.sub('{query}', res, tpl)
}

# traslates
translates_config = {
    'reg': r'(\w+)translate',
    'translater': {
        'baidu': {
            'url': 'http://fanyi.baidu.com/#en/zh/{keyword}',
            'tips': 'Results: {keyword}'
        }
    },
    'handler': lambda res,tpl: re.sub('{keyword}', res, tpl)
}


def error(msg = 'program occured a error'):
    print 'error:' + msg
    return msg

def responsePowerpack(res, argv):
    items = []
    data = []
    if isinstance(res, (list, tuple)):
        data = res
    else :
        data = [res]
    
    items = outputFormat(argv, data)

    response = {'items':items}
    return json.dumps(response)

def outputFormat(argv, data):
    # powerpack cmd
    cmd = argv[0]

    ret = candidatesFormat(argv, data)
    if ret == False:
        ret = translatesFormat(argv, data)
    if ret == False:
        ret = []
        for e in data:
            ret.append({
                'type' : 'default',
                'title' : e,
                'subtitle': '',
                'autocomplete' : e,
                'arg': e
            })
        


    return ret

def candidatesFormat(argv, data) :
    # query replacement
    tpl_render = candidates_config['handler']
    # searcher config
    searcher = False
    # powerpack cmd
    cmd = argv[0]
    # object list for powerpack
    ret = []
    # search keyword
    keyword = argv[1]

    searchers = candidates_config['searcher']
    # found searcher
    reg = candidates_config['reg']
    p = re.compile(reg, re.IGNORECASE)
    matched = p.match(cmd)
    if matched:
        searcher = searchers[matched.group(1)]
    # no matched searcher
    if not searcher:
        return False
    
    # formatting data (array) to popwerpack object list
    # default search
    ret.append({
        'type' : 'default',
        'title' : tpl_render(keyword, searcher['tips']),
        'subtitle': '',
        'autocomplete' : keyword,
        'arg': tpl_render(keyword, searcher['query'])
    })
    for e in data:
        data = {
            'type' : 'default',
            'title' : e,
            'subtitle': '',
            'autocomplete' : e,
            'arg': tpl_render(e, searcher['query'])
        }
        ret.append(data)
    return ret

def translatesFormat(argv, data):
     # keyword replacement
    tpl_render = translates_config['handler']
     # powerpack cmd
    cmd = argv[0]
    # object list for powerpack
    ret = []
    # search keyword
    keyword = argv[1]
    translater = False
    # found details
    reg = translates_config['reg']
    p = re.compile(reg, re.IGNORECASE)
    matched = p.match(cmd)
    if matched:
        translater = translates_config['translater'][matched.group(1)]
    # no matched translater
    if not translater:
        return False
    # formatting data (array) to popwerpack object list
    # default search
    translate_res = data['res']
    top_item_tpl = translater['tips']
    if len(data['correct']) > 0:
        top_item_tpl = 'Looking for "' + data['correct'] +'"?:{keyword}'
    
    ret.append({
        'type' : 'default',
        'title' : tpl_render(translate_res, top_item_tpl),
        'subtitle': 'Press enter to look details',
        'autocomplete' : keyword if len(data['correct']) == 0 else data['correct'],
        'arg': tpl_render(keyword, translater['url'])
    })
    for e in data['parts']:
        means = '; '.join(e['means'])
        title = e['part'] + ' ' + means
        data = {
            'type' : 'default',
            'title' : title,
            'subtitle': '',
            'autocomplete' : '',
            'arg': tpl_render(keyword, translater['url'])
        }
        ret.append(data)
    return ret