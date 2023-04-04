#!/usr/bin/python3
def copy_list(clst):
    return clst.copy() if isinstance(clst, list) else clst
