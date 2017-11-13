# network methods 
# Candidate words tips:
# baidu bing google
# 
# translation:
# 
# Encrypt/decrypt :
# aes
# 
# Format:
# tt

import urllib, urllib2, json, re

def baiduCandidate(text):
    url = "https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su"
    params = {
        'wd': text,
        'json': 1,
        'cb' : 'candidates',
        'ie': 'utf-8'
    }
    data = syncAjax(url, params)
    data = re.compile('^candidates\((.*)\);$').match(data).group(1)
    data = json.loads(data)
    candidates = data['s']
    for (i, e) in enumerate(candidates):
        candidates[i] = e.encode('utf-8')
    return candidates

def bingCandidate(text):
    url = "https://cn.bing.com/AS/Suggestions?pt=page.home&mkt=zh-cn&cp=1&cvid=3D5460BA17EE4941A87817964CEF9D87"
    params = {
        "qry" : text
    }
    data = syncAjax(url, params)
    lis = re.findall(r'<div class="sa_tm">(.*?)</div>', data)
    p = re.compile('(.*)<strong>(.*)</strong>', re.IGNORECASE)
    res = []
    for e in lis:
        groups = p.match(e).groups()
        res.append(groups[0] + groups[1])
    return res

def googleCandidate(text):
    url = "https://www.google.com/complete/search?client=psy-ab&hl=zh-CN&gs_rn=64&gs_ri=psy-ab&cp=1&gs_id=cx&xhr=t"
    params = {
        "q" : text
    }
    data = syncAjax(url, params)
    data = json.loads(data)
    condidates = data[1]
    return condidates

def taobaoCandidate(text):
    url = "https://suggest.taobao.com/sug?code=utf-8&k=1&area=c2c&bucketid=4"
    params = {
        "q" : text,
    }
    data = syncAjax(url, params)
    data = data.replace("\n", '')
    data = json.loads(data)
    res = data['result']
    candidates = []
    for e in res:
        candidates.append(e[0].encode('utf-8'))
    # for (i, e) in enumerate(candidates):
    #     candidates[i] = e.encode('utf-8')
    return candidates


def syncAjax(url, data = '', method = 'GET'):
    # stringify
    if isinstance(data, (object)):
        data = urllib.urlencode(data)
    
    if method == 'GET':
        # add params to url tail
        if url.find('?') < 0:
            url += '?'
        url += '&' + data
        req = urllib2.Request(url)
    else:
        req = urllib2.Request(url, data)

    res = urllib2.urlopen(req).read()
    return res
