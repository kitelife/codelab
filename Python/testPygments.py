from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

code = 'print "hello, Python"'
lexer = get_lexer_by_name("python", stripall=True)
formatter = HtmlFormatter(linenos=True, noclasses="True")
result = highlight(code, lexer, formatter)
print result
