from inspect import getmodule
import sys


def introspection_info(obj):
    return {
        'type': type(obj).__name__,
        'attributes': obj.__dir__,
        'methods': dir(obj),
        'module': getmodule(obj),
        'bytes': sys.getsizeof(obj),
        'display': sys.displayhook(obj),
        'refcount': sys.getrefcount(obj),
        'denominator': obj.denominator
    }


number_info = introspection_info(42)
print(number_info)