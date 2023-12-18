#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        num = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e),file=sys.stderr)
        return None
    else:
        return num
