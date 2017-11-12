import time, json

def error(msg = 'program occured a error'):
    print 'error:' + msg
    return msg

def responsePowerpack(res, argv):
    res = str(res)
    items = []
    items.append({
        'uid' :  str(time.time()),
        'type' : 'default',
        'title' : res,
        'subtitle': '',
        'autocomplete' : res,
        'arg': res
    })
    response = {'items':items}
    return json.dumps(response)