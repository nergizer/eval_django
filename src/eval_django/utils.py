import traceback

from django.http import HttpResponseBase
from django.urls import path, URLPattern
from typing_extensions import Callable, Any


def try_or[O](try_block: Callable[[],O],else_return : O) -> O:
    try:
        return try_block()
    except Exception:
        traceback.print_exc()
        return else_return

def spath(name : str,view : Callable[...,HttpResponseBase]) -> URLPattern:
    assert '/' not in name
    assert '<' not in name
    return path(name,view,name=name)