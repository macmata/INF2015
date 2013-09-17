class Rule(object):
    def __init__(self, quote):
        self.quote = quote

    def apply_rules(self):
        for module in dir(self):
            if module.startswith('rule_'):
                self.quote = getattr(self, module)()
