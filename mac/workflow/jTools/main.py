#!/usr/bin/python
import sys
import hashlib
origin_text=sys.argv[1]
md5=hashlib.md5()
md5.update(origin_text)
str_md5_16=md5.hexdigest()
print '''
{"items": [
    {
        "uid": "desktop",
        "type": "file",
        "title": "%s",
        "subtitle": "16 md5 for %s",
        "arg": "~/Desktop",

]}
''' % (str_md5_16,origin_text)
