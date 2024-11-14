import traceback

from django.http import HttpResponseBase
from django.urls import path, URLPattern
from typing_extensions import Callable, Any


def try_or[O](try_block: Callable[[],O],else_return : O) -> O:
    """Try to call lambda try_block, or return else_return in case of an excepetion
    The exception message is printed to stderr
    >>> try_or(lambda : 1/0,0)
    0
    >>> try_or(lambda : 1/2,-1)
    0.5
    >>> ex = lambda: ["a"][2]
    >>> try_or(ex,"Error")
    'Error'
    """
    try:
        return try_block()
    except BaseException:
        traceback.print_exc()
        return else_return

def spath(name : str,view : Callable[...,HttpResponseBase]) -> URLPattern:
    """Simple parameterless path util"""
    assert '/' not in name
    assert '<' not in name
    return path(name,view,name=name)