import sys
import pkgutil
import inspect

from builder.rules.rule import Rule

__all__ = ['Rule']
for loader, module_name, is_pkg in  pkgutil.walk_packages(__path__):
    __all__.append(module_name)
    setattr(sys.modules[__name__], module_name, loader.find_module(module_name).load_module(module_name))
