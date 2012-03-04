from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

code = 'print "Hello, World"'

lexer = get_lexer_by_name('python', stripall=True)
formatter = HtmlFormatter(linenos=True, cssclass="source")
print highlight(code, lexer, formatter)
