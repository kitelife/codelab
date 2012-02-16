import sys
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

def code2html(code, lang):
    lexer = get_lexer_by_name(lang, encoding='utf-8', stripall=True)
    formatter = HtmlFormatter(
        linenos=True,
        encoding='utf-8',
        noclasses="True")
    result = highlight(code, lexer, formatter)
    return result

def output_head():
    print '''
<!DOCTYPE html
PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
        <title>O_O</title>
        <!--<link rel="stylesheet" type="text/css" href="http://www.peerat.com/code/style.css" />-->
    </head>
    <body>
    '''
    
def output_end():
    print '</body>'
    print '</html>'
    
if __name__ == '__main__':
    print __file__
    output_head()
    f = open(__file__)
    code = f.read()
    f.close()
    print code2html(code, 'python')
    output_end()
