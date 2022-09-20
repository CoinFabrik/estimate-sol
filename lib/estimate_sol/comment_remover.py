class NormalState:
    @classmethod
    def process_char(cls, c):
        if "/" == c:
            return "", SlashState
        elif c in ("\"", "'"):
            return c, StringBody(quote=c)
        return c, cls

class IgnoreUntilCR:
    @classmethod
    def process_char(cls, c):
        if "\n" == c:
            return "\n", NormalState
        return "", IgnoreUntilCR

class SlashState:
    @classmethod
    def process_char(cls, c):
        if "/" == c:
            return "", IgnoreUntilCR
        elif "*" == c:
            return "", MultilineCommentBody
        return "/" + c, NormalState

class MultilineCommentBody:
    @classmethod
    def process_char(cls, c):
        if c == "*":
            return "", MultilineCommentAsterisk
        return "", cls

class MultilineCommentAsterisk:
    @classmethod
    def process_char(cls, c):
        if "/" == c:
            return "", NormalState
        elif "*" == c:
            return "", MultilineCommentAsterisk
        return "", MultilineCommentBody

class StringBody:
    def __init__(self, quote):
        self.quote = quote

    def process_char(self, c):
        if self.quote == c:
            return c, NormalState
        elif "\\" == c:
            return c, StringEscaped(quote=self.quote)
        
        return c, self

class StringEscaped:
    def __init__(self, quote):
        self.quote=quote

    def process_char(self, c):
        return c, StringBody(quote=self.quote)

def comment_remover(char_iter):
    state = NormalState
    for c in char_iter:
        chars, state = state.process_char(c)
        for c2 in chars:
            yield c2

def remove_comments(s):
    return ''.join(comment_remover(s))
