# native methods 
# Hash & encode/decode :
# md5, sha1, base64
#
# Encrypt/decrypt :
# aes
# 
# Format:
# tt
import hashlib, re, time, urllib, json
import base64 as b6


# Hash & encode/decode :
def md5(text):
    m = hashlib.md5()
    m.update(text)
    return m.hexdigest()

def sha1(text):
    m = hashlib.sha1()
    m.update(text)
    return m.hexdigest()

def base64(text):
    encode = b6.b64encode(text)
    decode = ''
    if len(text) % 4 == 0 and re.compile(r'^[A-Z0-9a-z+/]+=*$').match(text):
        try:
            decode = b6.b64decode(text)
        except :
            decode = ''
    return [encode, decode]

def urlcode(text):
    encode = urllib.quote(text)
    decode = urllib.unquote(text)
    return [encode, decode]

#-------------------------------
# Encrypt/decrypt :

def aes(text, pwd):
    pass

#-------------------------------

# timestamp to date or date to timestamp
def tt(text):
    if re.compile(r'^\d+$').match(text):
        timestamp = time.localtime(int(text))
        return time.strftime(r'%Y-%m-%d %H:%M:%S', timestamp)
    elif text == 'now':
        return int(time.time())
    else:
        time_array = time.strptime(text, r'%Y-%m-%d %H:%M:%S')
        return int(time.mktime(time_array))
