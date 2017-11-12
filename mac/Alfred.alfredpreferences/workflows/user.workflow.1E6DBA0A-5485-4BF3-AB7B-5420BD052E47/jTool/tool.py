# boot leader for jTool
import inspect, re
import jTool.native as native
from jTool.output import *


def call(argv):
    cmd = argv[0]
    parameters = argv[1:]
    parameters_str = []
    # format param to str
    for (i, e) in enumerate(parameters):
        parameters_str.append('parameters[' + str(i) + ']')
        
    
    if not cmd:
        return error()
    if hasattr(native, cmd):
        func_name = 'native.' + cmd
        arg_len = len(inspect.getargspec(eval(func_name)).args)
        if len(parameters_str) < arg_len:
            return error()
        statement = func_name+ '(' + ','.join(parameters_str[:arg_len]) + ')'
        res = eval(statement)
    else:
        return error()
    return res
