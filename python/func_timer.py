import functools
import time
import logging

logger = logging.getLogger(__name__)
def decorator(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kwargs):
        start = time.time()
        result =  fn(*args,**kwargs)
        during = time.time() - start
        action = logger.info
        if during >0.2 :
            action = logger.warn
        if during >2 :
            action = logger.error
        during  = str(during*1000)
        action("func::" + fn.func_name + ' cost ' + during + "ms.")
        return result
    return wrapper

