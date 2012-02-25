from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

html = """
<html>
<body>
    <form method="post" action="parsing_post.wsgi">
        <p>
        Age :<input type="text" name="age">
        </p>
        <p>
        Hobbies:
        <input name="hobbies" type="checkbox" value="software">Software
        <input name="hobbies" type="checkbox" value="tunning"> Auto Tunning
        </p>
        <p>
        <input type="submit" value="Submit">
        </p>
        <p>
        Age: %s<br>
        Hobbies: %s
        </p>
    </form>
</body>
</html>
"""

def application(environ, start_response):

    try:
        request_body_size = int(environ.get('CONTENT_LENGTH',0))
    except (ValueError):
        request_body_size = 0

    request_body = environ['wsgi.input'].read(request_body_size)
    d = parse_qs(request_body)

    age = d.get('age', [''])[0]
    hobbies = d.get('hobbies',[])

    age = escape(age)
    hobbies = [escape(hobby) for hobby in hobbies]

    response_body = html % (age or 'Empty',
                            ', '.join(hobbies or ['No Hobbies']))

    status = '200 OK'
    response_headers = [('Content-Type', 'text/html'),
                        ('Content-Length', str(len(response_body)))]

    start_response(status, response_headers)

    return [response_body]

httpd = make_server('localhost', 8888, application)
httpd.serve_forever()
