#!/usr/bin/python
from jTool import tool
import sys
query = sys.argv[1]
p = query.index(':')
cmd = query[:p]
query = query[p+1:]
args = [cmd, query]
res = tool.call(args)
print tool.responsePowerpack(res, args)
