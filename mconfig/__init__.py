import traceback
import yaml

class BasicError(Exception):
    """Docstring."""
    def __init__(self):
        self.message = "Missing the yml file"
    
    def __str__(self):
        return self.message

CONF_FILE = None

def __take__(k, v):
    if isinstance(k, str) and isinstance(v, dict):
        if k in v:
            return v[k]
    return None

def load(path=None):
    """set the YML File."""
    try:
        global CONF_FILE
        CONF_FILE = yaml.load(open(path, 'r'))
    except:
        print(traceback.print_exc())

def get(key, response=None):
    """Returns k:str to exist in the yml file, Otherwise it returns default."""
    try:
        global CONF_FILE

        if CONF_FILE:
            if isinstance(key, str):
                sb = key.strip('.').split('.')
                p = CONF_FILE
                for i in sb:
                    p = __take__(i, p)
                return p
        else:
            raise BasicError
    except:
        print(traceback.print_exc())
    return response
