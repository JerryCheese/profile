# native methods 
# Hash & encode/decode :
# md5, sha1, base64
#
# Encrypt/decrypt :
# aes
# 
# Format:
# tt
import hashlib
import base64 as b6
import re
import time


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
    return b6.b64encode(text)

def base64d(text):
    return b6.b64decode(text)
#-------------------------------
# Encrypt/decrypt :

def aes(text, pwd):
    pass

#-------------------------------

def tt(text):
    if re.compile(r'^\d+$').match(text):
        timestamp = time.localtime(int(text))
        return time.strftime(r'%Y-%m-%d %H:%M:%S', timestamp)
    elif text == 'now':
        return int(time.time())
    else:
        timeArray = time.strptime(text, r'%Y-%m-%d %H:%M:%S')
        return int(time.mktime(timeArray))
