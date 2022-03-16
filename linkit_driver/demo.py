import mraa
import time
import threading
import Queue
from cgi import parse_qs
from wsgiref.simple_server import make_server

status = {
    'FAN':0,
    'LIGHT':0,
    'DIFFUSER':0,
    'SOCKET':0,
}

gpio_socket = mraa.Gpio(43)
gpio_light = mraa.Gpio(1)
gpio_diffuser = mraa.Gpio(2)
gpio_fan = mraa.Gpio(3)

gpio_socket.dir(mraa.DIR_OUT)
gpio_light.dir(mraa.DIR_OUT)
gpio_diffuser.dir(mraa.DIR_OUT)
gpio_fan.dir(mraa.DIR_OUT)

q = Queue.Queue()

def doAction(queue):

    def statusConvert(status, is_fan):
        retVal = 0
        if status == 'off':
            retVal = 0
        if (status == 'slow') & (is_fan == True):
            retVal = 1
        if (status == 'normal') & (is_fan == True):
            retVal = 2
        if (status == 'high') & (is_fan == True):
            retVal = 3
        if (status == 'on') & (is_fan == False):
            retVal = 4
        
        return retVal

    print('In blink')
    gpio_def = ['SOCKET', 'LIGHT', 'DIFFUSER', 'FAN']
    while(1):
        print('Inside queue: ', queue.get())
        data = queue.get()['data']
        print(data)
        if (data):
            if data[0] == 'FAN':
                print('Fan: {}'.format(data[1]))
                if data[1] == 'on':        
                    gpio_fan.write(1)
                elif data[1] == 'off':
                    gpio_fan.write(0)
            if data[0] == 'LIGHT':
                print('Light: {}'.format(data[1]))
                if data[1] == 'on':
                    gpio_light.write(1)
                elif data[1] == 'off':
                    gpio_light.write(0)
            if data[0] == 'DIFFUSER':
                print('Diffuser: {}'.format(data[1]))
                if data[1] == 'on':
                    gpio_diffuser.write(1)
                elif data[1] == 'off':
                    gpio_diffuser.write(0)
            if data[0] == 'SOCKET':
                print('Socket: {}'.format(data[1]))
                if data[1] == 'on':
                    gpio_socket.write(1)
                elif data[1] == 'off':
                    gpio_socket.write(0)
        
        queue.task_done()
        
def gateway_handler(environ, start_response):
    print('listener')
    status = '200 OK'
    headers = [('Content-Type', 'text/plain:charset=utf-8')]
    start_response(status, headers)
    if environ['REQUEST_METHOD'] == 'POST':
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        request_body = environ['wsgi.input'].read(request_body_size)
        d = parse_qs(request_body)  # turns the qs to a dict\
        print(d) # For debugging
        q.put(d)
        # return 'From POST: %s' % ''.join('%s: %s' % (k, v) for k, v in d.iteritems())
        return 'From POST: {}'.format(d)
    else:  # GET
        d = parse_qs(environ['QUERY_STRING'])  # turns the qs to a dict
        print(d)
        # return 'From GET: %s' % ''.join('%s: %s' % (k, v) for k, v in d.iteritems())
        return 'From GET: {}'.format(d)


if __name__ == '__main__':
    httpd = make_server('', 1337, gateway_handler)
    # httpd.server_close()
    t1 = threading.Thread(target=httpd.serve_forever)
    t2 = threading.Thread(target=doAction, args=(q,))
    t1.start()
    t2.start()
    # t1 = threading.Thread(target=blinking, args=(gpio_socket,))
    # t2 = threading.Thread(target=blinking, args=(gpio_light,))
    # t3 = threading.Thread(target=blinking, args=(gpio_diffuser,))
    # t4 = threading.Thread(target=blinking, args=(gpio_fan,))
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
        