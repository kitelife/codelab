import sys
import socket
import time
import threading

def threads(port):
	s = socket.socket()
	s.bind(('0.0.0.0', port))
	s.listen(500)
	while True:
		cli, addr = s.accept()
		t = threading.Thread(target=handle_request, args=(cli, time.sleep))
		t.daemon = True
		t.start()

def handle_request(s, sleep):
	try:
		s.recv(1024)
		sleep(0.1)
		s.send('''HTTP/1.0 200 Ok

		Hello world''')
		s.shutdown(socket.SHUT_WR)
		print '.',
	except Exception, ex:
		print 'e', ex
	finally:
		sys.stdout.flush()
		s.close()

if __name__ == '__main__':
	threads(int(sys.argv[1]))
