class NormalState:
    @classmethod
    def process_char(cls, c):
        if c in ("\"", "'"):
            return c, StringBody(quote=c)

        return c, cls

class StringBody:
    def __init__(self, *, quote):
        self.quote = quote

    def process_char(self, c):
        if c == self.quote:
            return c, NormalState
        elif c == "\\":
            return "", Escaped(quote=self.quote)
        return "", self

class Escaped:
    def __init__(self, *, quote):
        self.quote = quote

    def process_char(self, c):
        return "", StringBody(quote=self.quote)

def string_blanker(char_iter):
    state = NormalState
    for c in char_iter:
        chars, state = state.process_char(c)
        for c2 in chars:
            yield c2

def blank_strings(s):
    return ''.join(string_blanker(s))