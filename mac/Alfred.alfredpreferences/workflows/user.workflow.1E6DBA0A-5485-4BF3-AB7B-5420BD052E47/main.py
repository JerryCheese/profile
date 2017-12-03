#!/usr/bin/python
import sys
import hashlib
origin_text=sys.argv[1]
md5=hashlib.md5()
#md5
md5.update(origin_text)
str_md5 = md5.hexdigest()
#md5(md5)
md5.update(str_md5)
str_md5_md5 = md5.hexdigest()
print '''
{"items": [
    {
        "uid": "md5-%s",
        "type": "file",
        "title": "%s",
        "subtitle": "md5 for %s",
        "autocomplete": "%s",
        "arg": "~/Desktop"
    },
    {
        "uid": "md5-md5-%s",
        "type": "file",
        "title": "%s",
        "subtitle": "md5's md5 for %s",
        "arg": "~/Desktop",
        "autocomplete": "%s"
    }
]}
''' % (origin_text, str_md5, origin_text, str_md5, origin_text, str_md5_md5, origin_text, str_md5_md5)
'''
JSON Format
{"items": [
    {
        "uid": "desktop",
        "type": "file",
        "title": "Desktop",
        "subtitle": "~/Desktop",
        "arg": "~/Desktop",
        "autocomplete": "Desktop",
        "icon": {
            "type": "fileicon",
            "path": "~/Desktop"
        }
    }
]}
'''