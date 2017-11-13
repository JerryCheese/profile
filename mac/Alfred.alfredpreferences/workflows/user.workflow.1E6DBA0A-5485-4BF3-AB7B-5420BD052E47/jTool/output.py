import time, json, re
import native

def error(msg = 'program occured a error'):
    print 'error:' + msg
    return msg

def responsePowerpack(res, argv):
    items = []
    data = []
    if isinstance(res, (list, tuple)):
        for e in res:
            data.append(e)
    else :
        data.append(res)
    
    for e in data:
        items.append(outputFormat(argv[0], e))
    response = {'items':items}
    return json.dumps(response)

def outputFormat(cmd, res):
    data = {
        'uid' :  native.md5(res),
        'type' : 'default',
        'title' : res,
        'subtitle': '',
        'autocomplete' : res,
        'arg': res
    }
    # reg for jump to url
    jump = [
        {
            'reg': r'(\w+)candidate$',
            'urltplmap': {
                'baidu': 'https://www.baidu.com/s?ie=UTF-8&wd={query}',
                'bing': 'https://cn.bing.com/search?q={query}',
                'google': 'https://www.baidu.com/s?ie=UTF-8&wd={query}',
                'taobao': 'https://s.taobao.com/search?q={query}'
                
            },
            'handler': lambda data,res,tpl: re.sub('{query}', res, tpl)
        }
    ]

    for e in jump:
        reg = e['reg']
        urltplmap = e['urltplmap']
        
        p = re.compile(reg, re.IGNORECASE)
        matched = p.match(cmd)
        if matched:
            urltpl = urltplmap[matched.group(1)]
            data['arg'] = e['handler'](data, res, urltpl)
    return data
