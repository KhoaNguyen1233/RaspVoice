import time
import signal
import threading
from cgi import parse_qs
from wsgiref.simple_server import make_server

status = {
    'FAN':0,
    'LIGHT':0,
    'DIFFUSER':0,
    'SOCKET':0,
}

def simple_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain:charset=utf-8')]
    start_response(status, headers)
    if environ['REQUEST_METHOD'] == 'POST':
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        request_body = environ['wsgi.input'].read(request_body_size)
        d = parse_qs(request_body)  # turns the qs to a dict\
        print(d['data'][0])
        # return 'From POST: %s' % ''.join('%s: %s' % (k, v) for k, v in d.iteritems())
        return 'From POST: {}'.format(d)
    else:  # GET
        d = parse_qs(environ['QUERY_STRING'])  # turns the qs to a dict
        print(d)
        # return 'From GET: %s' % ''.join('%s: %s' % (k, v) for k, v in d.iteritems())
        return 'From GET: {}'.format(d)

def test_thread(msg):
    while(1):
        print(msg)
        time.sleep(0.5)

if __name__ == "__main__":

    httpd = make_server('', 1337, simple_app)
    # httpd.server_close()
    t1 = threading.Thread(target=httpd.serve_forever)
    t2 = threading.Thread(target=test_thread, args=("Can do futher things",))
    t1.start()
    t2.start()