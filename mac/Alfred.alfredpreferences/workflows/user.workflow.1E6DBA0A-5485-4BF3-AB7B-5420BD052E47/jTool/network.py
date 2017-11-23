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

# candidates
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
        candidates[i] = e
    if len(candidates) == 0:
        candidates.append(text)
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
        matched = p.match(e)
        if matched:
            groups = matched.groups()
            res.append(groups[0] + groups[1])
    if len(res) == 0:
        res.append(text)
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
        candidates.append(e[0])
    if len(candidates) == 0:
        candidates.append(text)
    return candidates


# translate
def baiduTranslateChinese(text):
    return baiduTranslate(text,'zh')

def baiduTranslateEnglish(text):
    return baiduTranslate(text,'en', baiduTranslateEnglishSymbolHandler)

def baiduTranslateEnglishSymbolHandler(data, inspect_res, correct_res):
    ret = {
        'res': '',
        # correct text for input text
        'correct': '',
        # parts : [{means:'', part:''}], 'means' as translate results, 'part' as specific classification of words
        'parts': [],
        'audio': {}
    }
    ret['res'] = data['trans_result']['data'][0]['dst']
    if correct_res['origtxt'] != correct_res['correctxt']:
        ret['correct'] = correct_res['correctxt']

    if data['dict_result'] and data['dict_result'].has_key('simple_means'):
        symbols = data['dict_result']['simple_means']['symbols'][0]
        parts = symbols['parts']
        for (i, e) in enumerate(parts):
            parts[i]['part'] = e['part_name'] + ('.' if len(e['part_name']) > 0 else '')
            parts_means = parts[i]['means']
            means = []
            for (i2, e2) in enumerate(parts_means):
                means.append(e2['text'])
            parts[i]['means'] = means 
        ret['parts'] = parts
    return ret

def baiduTranslateJapanese(text):
    return baiduTranslate(text,'jp')

def baiduTranslate(text, target_lan = 'zh', symbol_handler = False):
    inspect_url = "http://fanyi.baidu.com/langdetect"
    params = {
        'query': text
    }
    inspect_res = syncAjax(inspect_url, params)
    inspect_res = json.loads(inspect_res)

    correct_url = "http://correctxt.baidu.com/correctxt?"
    params = {
        'callback':'cb',
        'text':text, 
        'ie': 'utf-8',
        'version':0,
        'from': 'FanyiWeb'
    }
    correct_res = syncAjax(correct_url, params)
    correct_res = re.compile('^/\*\*/cb\((.*)\)$').match(correct_res).group(1)
    correct_res = json.loads(correct_res)


    translate_url = "http://fanyi.baidu.com/v2transapi"
    params = {
        'from': inspect_res['lan'],
        'to': target_lan,
        'query': text,
        'transtype': 'translang',
        'simple_means_flag': 3
    }
    data = syncAjax(translate_url, params)
    data = json.loads(data)
    ret = {
        'res': '',
        # correct text for input text
        'correct': '',
        # parts : [{means:'', part:''}], 'means' as translate results, 'part' as specific classification of words
        'parts': [],
        'audio': {}
    }

    if callable(symbol_handler):
        ret = symbol_handler(data, inspect_res, correct_res)
    else :
        ret['res'] = data['trans_result']['data'][0]['dst']
        if correct_res['origtxt'] != correct_res['correctxt']:
            ret['correct'] = correct_res['correctxt']
        
        if data['dict_result'] and data['dict_result'].has_key('simple_means'):
            symbols = data['dict_result']['simple_means']['symbols']
            ret['parts'] = symbols[0]['parts']
            for (i, e) in enumerate(ret['parts']):
                means = ret['parts'][i]['means']
                for (i2, e2) in enumerate(means):
                    means[i2] = e2
                ret['parts'][i]['part'] = e['part']
    return ret





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
