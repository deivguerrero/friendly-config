import traceback
import yaml

CONF_FILE = None

try:
    CONF_FILE = yaml.load(open('conf.yml', 'r'))
except:
    print(traceback.print_exc())
    CONF_FILE = None

def __take__(k, v):
    if isinstance(k, str) and isinstance(v, dict):
        if k in v:
            return v[k]
    return None

def get(key, default=None):
    """Returns k:str to exist in the yml file, Otherwise it returns default."""
    try:
        if isinstance(key, str) and CONF_FILE:
            sb = key.strip('.').split('.')
            p = CONF_FILE
            for i in sb:
                p = __take__(i, p)
            return p
    except:
        print(traceback.print_exc())
    return default
