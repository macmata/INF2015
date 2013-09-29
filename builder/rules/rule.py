import logging
import sys


class Rule(object):
    def __init__(self, quote):
        self.quote = quote

    def apply_rules(self):
        for module in dir(self):
            if module.startswith('rule_'):
                logging.debug('Calling rule %s.%s' % (self.__class__.__name__, module))
                getattr(self, module)()
